# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2015, 2016, 2017 CERN.
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

# Use CentOS7:
FROM centos:7

# Install CERN Open Data Portal web node pre-requisites:
RUN yum update -y && \
    yum install -y \
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
        libxml2-devel \
        libxslt-devel \
        npm \
        python-devel \
        python-pip  && \
    yum install -y \
        xrootd \
        xrootd-client \
        xrootd-client-devel \
        xrootd-python && \
    yum clean -y all

# Configuration for CERN Open Data Portal instance:
ENV APP_INSTANCE_PATH=/usr/local/var/cernopendata/var/cernopendata-instance

RUN pip install --upgrade pip setuptools wheel && \
    npm install -g node-sass@3.8.0 clean-css@3.4.24 requirejs uglify-js

ADD requirements-production-local-forks.txt /tmp
ADD requirements-production.txt /tmp
RUN pip install -r /tmp/requirements-production-local-forks.txt
RUN pip install -r /tmp/requirements-production.txt

# Add CERN Open Data Portal sources to `code` and work there:
WORKDIR /code
ADD . /code

RUN /code/scripts/create-instance.sh && \
    chgrp -R 0 ${APP_INSTANCE_PATH} && \
    chmod -R g=u ${APP_INSTANCE_PATH}

RUN adduser --uid 1000 invenio --gid 0 && \
    chown -R invenio:root /code
USER 1000

ARG UWSGI_WSGI_MODULE=cernopendata.wsgi:application
ENV UWSGI_WSGI_MODULE ${UWSGI_WSGI_MODULE}
ARG UWSGI_PORT=5000
ENV UWSGI_PORT ${UWSGI_PORT}
ARG UWSGI_PROCESSES=2
ENV UWSGI_PROCESSES ${UWSGI_PROCESSES}
ARG UWSGI_THREADS=2
ENV UWSGI_THREADS ${UWSGI_THREADS}

# Start the CERN Open Data Portal application:
CMD uwsgi --module ${UWSGI_WSGI_MODULE} --http-socket 0.0.0.0:${UWSGI_PORT} --master --processes ${UWSGI_PROCESSES} --threads ${UWSGI_THREADS} --stats /tmp/stats.socket
