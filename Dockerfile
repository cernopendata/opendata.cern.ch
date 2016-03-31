# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2015, 2016 CERN.
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

# Use Python-2.7:
FROM python:2.7-slim

COPY scripts/provision-web.sh /tmp/

# Install CERN Open Data Portal web node pre-requisites:
RUN /tmp/provision-web.sh

# Add CERN Open Data Portal sources to `code` and work there:
WORKDIR /code
ADD . /code

# Run container as user `invenio` with UID `1000`, which should match
# current host user in most situations:
RUN adduser --uid 1000 --disabled-password --gecos '' invenio && \
    chown -R invenio:invenio /code
USER invenio

# Create CERN Open Data Portal instance:
RUN . /code/.inveniorc-docker; /code/scripts/create-instance.sh --devel

# Make given VENV default:
ENV PATH=/home/invenio/.virtualenvs/cernopendata/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python
RUN echo "source /usr/local/bin/virtualenvwrapper.sh\nworkon cernopendata" >> ~/.bashrc

VOLUME /code
VOLUME /home/invenio

# Start the CERN Open Data Portal application:
CMD ["/bin/bash", "-c", "cernopendata run -h 0.0.0.0"]
