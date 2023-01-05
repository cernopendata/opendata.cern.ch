# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2015, 2016, 2017, 2018, 2020, 2021, 2022, 2023 CERN.
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

# Use CentOS7
FROM centos:7

# Install Node.js 6 from Nodesource early. Doing so after installing EPEL7
# would make Nodesource to not recognise anymore the system as a supported
# CentOS7 installation.
# hadolint ignore=DL3033,DL4006
RUN curl -sL https://rpm.nodesource.com/setup_6.x | bash - && \
    yum install -y \
        nodejs && \
    yum clean all

# Install CERN Open Data Portal web node pre-requisites
# hadolint ignore=DL3033
RUN yum install -y \
        ca-certificates \
        curl \
        git \
        rlwrap && \
    yum install -y \
        centos-release-scl \
        epel-release && \
    yum groupinstall -y "Development Tools" && \
    yum install -y \
        cmake3 \
        devtoolset-7-gcc-c++ \
        jq \
        libffi-devel \
        libuuid-devel \
        libxml2-devel \
        libxslt-devel \
        openssl-devel \
        python-devel \
        python-pip \
        python2-xrootd-5.5.1 \
        xrootd-5.5.1\
        xrootd-client-5.5.1 \
        xrootd-client-devel-5.5.1 && \
    yum clean all

# Configuration for CERN Open Data Portal instance
ENV APP_INSTANCE_PATH=/usr/local/var/cernopendata/var/cernopendata-instance

# Upgrade pip and install some python/node packages
# hadolint ignore=DL3016
RUN pip install --no-cache-dir --upgrade pip==20.3.4 setuptools==44.1.1 wheel==0.37.1 && \
    npm install -g node-sass@3.8.0 clean-css@3.4.24 requirejs uglify-js jsonlint

# Install older version of pkgconfig, necessary for Python-2.7
RUN pip install --no-cache-dir pkgconfig==1.5.2

# Install xrootd 4.12.7 and xrootdpyfs 0.2.2
RUN pip install --no-cache-dir xrootd==4.12.7 xrootdpyfs==0.2.2

# Install requirements
COPY requirements-production-local-forks.txt /tmp
COPY requirements-production.txt /tmp
RUN pip --no-cache-dir install -r /tmp/requirements-production-local-forks.txt && \
    pip --no-cache-dir install -r /tmp/requirements-production.txt

# Add CERN Open Data Portal sources to `code` and work there
WORKDIR /code
COPY . /code

# Create instance
RUN /code/scripts/create-instance.sh && \
    chgrp -R 0 ${APP_INSTANCE_PATH} && \
    chmod -R g=u ${APP_INSTANCE_PATH}

# Condigure uWSGI
ARG UWSGI_WSGI_MODULE=cernopendata.wsgi:application
ENV UWSGI_WSGI_MODULE ${UWSGI_WSGI_MODULE:-cernopendata.wsgi:application}
ARG UWSGI_PORT=5000
ENV UWSGI_PORT ${UWSGI_PORT:-5000}
ARG UWSGI_PROCESSES=2
ENV UWSGI_PROCESSES ${UWSGI_PROCESSES:-2}
ARG UWSGI_THREADS=2
ENV UWSGI_THREADS ${UWSGI_THREADS:-2}

# Debug off by default
ARG DEBUG=""
ENV DEBUG=${DEBUG:-""}

# Install Python packages needed for development
RUN if [ "$DEBUG" ]; then pip install --no-cache-dir -r requirements-dev.txt; fi;

# Change user from root to invenio for better security
RUN adduser --uid 1000 invenio --gid 0 && \
    chown -R invenio:root /code
USER 1000

# Start the CERN Open Data Portal application
# hadolint ignore=DL3025
CMD uwsgi --module ${UWSGI_WSGI_MODULE} --socket 0.0.0.0:${UWSGI_PORT} --master --processes ${UWSGI_PROCESSES} --threads ${UWSGI_THREADS} --stats /tmp/stats.socket
