#!/bin/bash

set -e

# first check if we're passing flags, if so
# prepend with sentry
if [ "${1:0:1}" = '-' ]; then
    set -- sentry "$@"
fi

case "$1" in
    init_and_run)

        # Check that Postgresql is available to connect
        until PGPASSWORD="$SENTRY_DB_PASSWORD" psql -h "$SENTRY_POSTGRES_HOST" -U ${SENTRY_DB_USER} -c '\q'; do
          >&2 echo "Postgres is unavailable - sleeping 1 second..."
          sleep 1
        done

        # Initialize basic database structure for Sentry.
        # Note that using `--noinput` option when database is not
        # initialized will give a stack trace. This doesn't cause any trouble
        # and stack trace can be ignored.
        sentry upgrade --noinput

        # Add default values for first start wizard.
        # Note this doesn't get rid of the actual first start wizard
        # --> you still have to click continue in the UI on first run.
        sentry import /initialize.json

        # Create user and project and set up public_key and secret_key of the
        # project to 'test_public_key:test_secret_key' (for DSN).
        # Use http://<test_public_key:test_secret_key@container_name/sentry/2>
        # to connect to Sentry from clients.
        python /initialize.py

        # Run upgrade again just to make sure that initialization script
        # has not messed up application state or database content.
        sentry upgrade --noinput

        # Run Sentry web interface (API and UI)
        set -- sentry run web
    ;;
    run)

        # Checks if Sentry web interface is available, by polling healthcheck
        # endpoint provided by web interface.
        # Needed to prevent Sentry celery, cron or smtp from starting before
        # database has been initialized (in `init_and_run`).
        if [[ "$2" == "cron" || "$2" == "smtp" || "$2" == "worker" ]]; then
		    until [[ `wget -qO /dev/stdout http://sentry:9000/_health` == "ok" ]]; do
              >&2 echo "Sentry is unavailable - sleeping 5 seconds..."
              sleep 5
            done
		fi

        set -- sentry "$@"
    ;;
	celery|cleanup|config|createuser|devserver|django|exec|export|help|import|init|plugins|queues|repair|start|shell|tsdb|upgrade)
		set -- sentry "$@"
	;;
esac

if [ "$1" = 'sentry' ]; then
	set -- tini -- "$@"
	if [ "$(id -u)" = '0' ]; then
		mkdir -p "$SENTRY_FILESTORE_DIR"
		chown -R sentry "$SENTRY_FILESTORE_DIR"
		set -- gosu sentry "$@"
	fi
fi

exec "$@"

