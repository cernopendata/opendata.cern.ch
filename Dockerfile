# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2015, 2016, 2017, 2018, 2020, 2021, 2023, 2024 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Open Data Portal; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

# hadolint ignore=DL3007
FROM registry.cern.ch/cernopendata/cernopendata-portal:latest

# Add CERN Open Data Portal sources to `code` and work there
WORKDIR ${CODE_DIR}
COPY . ${CODE_DIR}
USER root
RUN chown -R "${INVENIO_USER_ID}":root "${CODE_DIR}"
USER ${INVENIO_USER_ID}

# Debug off by default
ARG DEBUG=""
ENV DEBUG=${DEBUG:-""}

# Install CERN Open Data Portal sources
# hadolint ignore=DL3013
RUN if [ "$DEBUG" ]; then FLAGS="-e"; fi && \
    pip install --user ${FLAGS} ".[all]" && pip check
# Create instance
RUN scripts/create-instance.sh

# Configure uWSGI
ARG UWSGI_BUFFER_SIZE=8192
ENV UWSGI_BUFFER_SIZE ${UWSGI_BUFFER_SIZE:-8192}
ARG UWSGI_IDLE=60
ENV UWSGI_IDLE ${UWSGI_IDLE:-60}
ARG UWSGI_MAX_REQUESTS=1000
ENV UWSGI_MAX_REQUESTS ${UWSGI_MAX_REQUESTS:-1000}
ARG UWSGI_MAX_WORKER_LIFETIME=1800
ENV UWSGI_MAX_WORKER_LIFETIME ${UWSGI_MAX_WORKER_LIFETIME:-1800}
ARG UWSGI_PORT=5000
ENV UWSGI_PORT ${UWSGI_PORT:-5000}
ARG UWSGI_PROCESSES=4
ENV UWSGI_PROCESSES ${UWSGI_PROCESSES:-4}
ARG UWSGI_THREADS=1
ENV UWSGI_THREADS ${UWSGI_THREADS:-1}
ARG UWSGI_WSGI_MODULE=cernopendata.wsgi:application
ENV UWSGI_WSGI_MODULE ${UWSGI_WSGI_MODULE:-cernopendata.wsgi:application}

# Start the CERN Open Data Portal application
# hadolint ignore=DL3025
CMD uwsgi \
        --buffer-size ${UWSGI_BUFFER_SIZE} \
        --cheap \
        --die-on-term \
        --enable-threads \
        --idle ${UWSGI_IDLE} \
        --master \
        --max-requests ${UWSGI_MAX_REQUESTS} \
        --max-worker-lifetime ${UWSGI_MAX_WORKER_LIFETIME} \
        --memory-report \
        --module ${UWSGI_WSGI_MODULE} \
        --need-app \
        --processes ${UWSGI_PROCESSES} \
        --py-call-osafterfork \
        --single-interpreter \
        --socket 0.0.0.0:${UWSGI_PORT} \
        --stats /tmp/stats.socket \
        --threads ${UWSGI_THREADS} \
        --vacuum \
        --wsgi-disable-file-wrapper
