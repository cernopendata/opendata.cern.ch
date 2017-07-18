#!/bin/bash
if ! whoami &> /dev/null; then
  if [ -w /etc/passwd ]; then
    echo "${LOGIN:-invenio}:x:$(id -u):0:${LOGIN:-invenio} user:${HOME}:/sbin/nologin" >> /etc/passwd
  fi
fi
source /usr/bin/virtualenvwrapper.sh
workon $INVENIO_WEB_INSTANCE
exec "$@"
