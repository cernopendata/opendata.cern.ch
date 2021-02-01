#!/usr/bin/env bash
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016, 2017, 2020 CERN.
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

set -o errexit
set -o nounset

mkdir -p "${INVENIO_INSTANCE_PATH}"
cd "${INVENIO_INSTANCE_PATH}"/static

npm install git+https://github.com/cernopendata/demobbed-viewer.git --prefix $INVENIO_INSTANCE_PATH/static
npm install ispy-webgl@0.9.8-COD3.11 --prefix $INVENIO_INSTANCE_PATH/static

cd node_modules/demobbed-viewer \
    && rm index.html LICENCE README.md package.json \
    && cd "${INVENIO_INSTANCE_PATH}"/static

cd node_modules/ispy-webgl \
    && rm index.html LICENSE README.md package.json \
    && cd "${INVENIO_INSTANCE_PATH}"/static \
    && rm package-lock.json

cernopendata collect -v
cernopendata webpack clean buildall
