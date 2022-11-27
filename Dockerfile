# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2015, 2016, 2017, 2018, 2020, 2021 CERN.
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

# Use Invenio's CentOS7 image with Python-3.6
FROM inveniosoftware/centos7-python:3.6

# Use XRootD 4.12.2
ENV XROOTD_VERSION=4.12.2

# Install CERN Open Data Portal web node pre-requisites
# hadolint ignore=DL3033
RUN yum install -y \
        ca-certificates \
        cmake \
        curl \
        git \
        rlwrap \
        screen \
        vim \
        emacs-nox && \
    yum install -y \
        epel-release && \
    yum groupinstall -y "Development Tools" && \
    yum --setopt=obsoletes=0 install -y \
        cmake gcc-c++ zlib-devel openssl-devel libuuid-devel python3-devel jq \
        openssl-devel \
        https://storage-ci.web.cern.ch/storage-ci/xrootd/release/cc-7-x86_64/v${XROOTD_VERSION}/xrootd-libs-${XROOTD_VERSION}-1.el7.x86_64.rpm \
        https://storage-ci.web.cern.ch/storage-ci/xrootd/release/cc-7-x86_64/v${XROOTD_VERSION}/xrootd-client-libs-${XROOTD_VERSION}-1.el7.x86_64.rpm \
        https://storage-ci.web.cern.ch/storage-ci/xrootd/release/cc-7-x86_64/v${XROOTD_VERSION}/xrootd-devel-${XROOTD_VERSION}-1.el7.x86_64.rpm \
        https://storage-ci.web.cern.ch/storage-ci/xrootd/release/cc-7-x86_64/v${XROOTD_VERSION}/xrootd-client-${XROOTD_VERSION}-1.el7.x86_64.rpm \
        https://storage-ci.web.cern.ch/storage-ci/xrootd/release/cc-7-x86_64/v${XROOTD_VERSION}/xrootd-client-devel-${XROOTD_VERSION}-1.el7.x86_64.rpm \
        https://storage-ci.web.cern.ch/storage-ci/xrootd/release/cc-7-x86_64/v${XROOTD_VERSION}/python3-xrootd-${XROOTD_VERSION}-1.el7.x86_64.rpm && \
    yum clean -y all

RUN pip uninstall pipenv -y && pip install --upgrade pip==20.2.4 setuptools==51.0.0 wheel==0.36.2 && \
    npm install -g --unsafe-perm node-sass@4.14.1 clean-css@3.4.24 requirejs@2.3.6 uglify-js@3.12.1 jsonlint@1.6.3 d3@6.3.1

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
RUN pip install --user xrootd==${XROOTD_VERSION} xrootdpyfs==0.2.1

# Install requirements
COPY requirements-production-local-forks.txt /tmp
COPY requirements-production.txt /tmp
RUN pip install --user -r /tmp/requirements-production-local-forks.txt
RUN pip install --user -r /tmp/requirements-production.txt

# Add CERN Open Data Portal sources to `code` and work there
WORKDIR ${CODE_DIR}
COPY . ${CODE_DIR}
USER root
RUN chown -R "${INVENIO_USER_ID}":root "${CODE_DIR}"
USER ${INVENIO_USER_ID}

# Debug off by default
ARG DEBUG=""
ENV DEBUG=${DEBUG:-""}

# hadolint ignore=DL3013
RUN if [ "$DEBUG" ]; then pip install --user -e ".[all]"; else pip install --user ".[all]"; fi;

# Create instance
RUN scripts/create-instance.sh

# Condigure uWSGI
ARG UWSGI_WSGI_MODULE=cernopendata.wsgi:application
ENV UWSGI_WSGI_MODULE ${UWSGI_WSGI_MODULE:-cernopendata.wsgi:application}
ARG UWSGI_PORT=5000
ENV UWSGI_PORT ${UWSGI_PORT:-5000}
ARG UWSGI_PROCESSES=2
ENV UWSGI_PROCESSES ${UWSGI_PROCESSES:-2}
ARG UWSGI_THREADS=2
ENV UWSGI_THREADS ${UWSGI_THREADS:-2}

# Install Python packages needed for development
RUN if [ "$DEBUG" ]; then pip install --user -r requirements-dev.txt; fi;

# Start the CERN Open Data Portal application
# hadolint ignore=DL3025
CMD [ "bash", "-c", "uwsgi --module ${UWSGI_WSGI_MODULE} --socket 0.0.0.0:${UWSGI_PORT} --master --processes ${UWSGI_PROCESSES} --threads ${UWSGI_THREADS} --stats /tmp/stats.socket" ]
