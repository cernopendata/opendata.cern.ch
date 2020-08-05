# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2015, 2016, 2017, 2018, 2020 CERN.
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

# Install CERN Open Data Portal web node pre-requisites
RUN yum update -y && \
    yum install -y \
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
    yum install -y \
        libffi-devel \
        libuuid-devel \
        libxml2-devel \
        libxslt-devel \
        npm \
        openssl-devel \
        jq \
        python-devel \
        python-pip

# Install latest stable xrootd 4.12.3 version and its dependencies
RUN yum install -y \
        xrootd-4.12.3 \
        xrootd-client-4.12.3 \
        xrootd-client-devel-4.12.3 \
        xrootd-python-4.12.3

# Clean after ourselves
RUN yum clean -y all

# Configuration for CERN Open Data Portal instance
ENV APP_INSTANCE_PATH=/usr/local/var/cernopendata/var/cernopendata-instance

# Upgrade pip and install some python/node packages
RUN pip install --upgrade pip==9 setuptools==42.0.2 wheel==0.33.6 && \
    npm install -g node-sass@3.8.0 clean-css@3.4.24 requirejs uglify-js jsonlint

# Install xrootdpyfs from GitHub, since xrootd-4.12.3-compatible version was not released on PyPI yet
RUN pip install xrootd==4.12.3 \
      'git+https://github.com/inveniosoftware/xrootdpyfs.git@1151a7a4c219dad11eb0020af4c19f94928469e3#egg=xrootdpyfs'

# Install requirements
ADD requirements-production-local-forks.txt /tmp
ADD requirements-production.txt /tmp
RUN pip install -r /tmp/requirements-production-local-forks.txt
RUN pip install -r /tmp/requirements-production.txt

# Add CERN Open Data Portal sources to `code` and work there
WORKDIR /code
ADD . /code

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
RUN if [ "$DEBUG" ]; then pip install -r requirements-dev.txt; fi;

# Change user from root to invenio for better security
RUN adduser --uid 1000 invenio --gid 0 && \
    chown -R invenio:root /code
USER 1000

# Start the CERN Open Data Portal application
CMD uwsgi --module ${UWSGI_WSGI_MODULE} --socket 0.0.0.0:${UWSGI_PORT} --master --processes ${UWSGI_PROCESSES} --threads ${UWSGI_THREADS} --stats /tmp/stats.socket
