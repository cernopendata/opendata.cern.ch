# This file is part of CERN Open Data Portal.
# Copyright (C) 2015 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

# based on the right Invenio base image
FROM invenio:2.0

# get root rights again
USER root

# add content
ADD . /code-overlay
WORKDIR /code-overlay

# fix requirements.txt and install additional dependencies
RUN sed -i '/inveniosoftware\/invenio[@#]/d' requirements.txt && \
    pip install -r requirements.txt --exists-action i

# step back
# in general code should not be writeable, especially because we are using
# `pip install -e`
RUN mkdir -p /code-overlay/src && \
    chown -R invenio:invenio /code-overlay && \
    chown -R root:root /code-overlay/invenio_opendata && \
    chown -R root:root /code-overlay/setup.* && \
    chown -R root:root /code-overlay/src

# finally step back again
USER invenio
