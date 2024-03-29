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

# Use Invenio's alma image with Python-3.9
FROM registry.cern.ch/inveniosoftware/almalinux:1

# Use XRootD 5.6.9
ENV XROOTD_VERSION=5.6.9

# Install CERN Open Data Portal web node pre-requisites
# hadolint ignore=DL3033
RUN yum install -y \
        ca-certificates \
        cmake3 \
        epel-release \
        libuuid-devel \
        rlwrap \
        vim && \
    yum groupinstall -y "Development Tools" && \
    yum clean -y all

RUN echo "Will install xrootd version: $XROOTD_VERSION (latest if empty)" && \
    yum install -y xrootd-"$XROOTD_VERSION" python3-xrootd-"$XROOTD_VERSION" && \
    yum clean -y all

RUN pip uninstall pipenv -y && pip install --upgrade pip==20.2.4 setuptools==68.2.2 wheel==0.36.2 && \
    npm install -g --unsafe-perm node-sass@6.0.1 clean-css@3.4.24 requirejs@2.3.6 uglify-js@3.12.1 jsonlint@1.6.3 d3@6.3.1

# Change group to root to support OpenShift runtime
RUN chgrp -R 0 "${INVENIO_INSTANCE_PATH}" && \
    chmod -R g=u "${INVENIO_INSTANCE_PATH}"

# Create `code` dir and set Invenio user as owner
ENV CODE_DIR=/code
RUN mkdir ${CODE_DIR} && chown invenio:root ${CODE_DIR}

# Run application as Invenio user
USER ${INVENIO_USER_ID}

# Set default Invenio user Python base for site-packages
ENV PYTHONUSERBASE=${INVENIO_INSTANCE_PATH}/python

# Add Invenio user Python base to global PATH
ENV PATH=$PATH:${INVENIO_INSTANCE_PATH}/python/bin

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
