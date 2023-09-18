FROM docker.io/library/sentry:8.22

RUN apt-get update && \
    apt-get install wget -y

# Add wget and postgresql-client since they are needed in docker-entrypoint.sh
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O- | apt-key add - && \
    echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' >> /etc/apt/sources.list.d/postgresql.list && \
    apt-get update && \
    apt-get install postgresql-client -y

# At minimum these environment variables should be set, otherwise
# docker-entrypoint won't work.
ENV SENTRY_SECRET_KEY=more_than_thirty_two_characters_long_secret_key
ENV SENTRY_POSTGRES_HOST=postgres
ENV SENTRY_DB_USER=postgres
ENV SENTRY_DB_PASSWORD=postgres

COPY docker-entrypoint.sh /entrypoint.sh
COPY initialize.py /initialize.py
COPY initialize.json /initialize.json
COPY sentry.conf.py /sentry.conf.py
COPY config.yml /config.yml

RUN if [ -s sentry.conf.py ]; then cp sentry.conf.py $SENTRY_CONF/; fi && \
    if [ -s config.yml ]; then cp config.yml $SENTRY_CONF/; fi

# Default CMD and ENTRYPOINT definitions come from Sentry baseimage
