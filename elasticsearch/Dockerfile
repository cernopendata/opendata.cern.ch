# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

# By default use Elasticsearch 2.
ARG ES_VERSION=2

# Select base image based on ES_VERSION BUILD ARGUMENT
# ('--build-arg', not '-e')
FROM elasticsearch:$ES_VERSION

# Because of Docker's multi-staged build ARGs defined before FROM will be
# in some sense "flushed" to empty or default values, so ARG ES_VERSION
# needs to be set again. (for info see https://github.com/docker/cli/pull/333)

ARG ES_VERSION=2

# Build arguments are not available in shell started with RUN.
# We need to set it to ENV_VAR.
ENV ES_VERSION=${ES_VERSION:-2}

COPY scripts/provision-elasticsearch.sh /tmp/

# Install Elasticsarch plugins:
RUN /tmp/provision-elasticsearch.sh
