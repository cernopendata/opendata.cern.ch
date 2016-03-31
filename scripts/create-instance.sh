#!/usr/bin/env bash
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016 CERN.
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

# check environment variables:
if [ -v ${INVENIO_WEB_INSTANCE} ]; then
    echo "[ERROR] Please set environment variable INVENIO_WEB_INSTANCE before runnning this script."
    echo "[ERROR] Example: export INVENIO_WEB_INSTANCE=invenio3"
    exit 1
fi
if [ -v ${INVENIO_WEB_VENV} ]; then
    echo "[ERROR] Please set environment variable INVENIO_WEB_VENV before runnning this script."
    echo "[ERROR] Example: export INVENIO_WEB_VENV=invenio3"
    exit 1
fi

# load virtualenvrapper:
source $(which virtualenvwrapper.sh)

# detect pathname of this script:
scriptpathname=$(cd "$(dirname $0)" && pwd)

# sphinxdoc-create-virtual-environment-begin
mkvirtualenv ${INVENIO_WEB_VENV}
# sphinxdoc-create-virtual-environment-end

# quit on errors and unbound symbols:
set -o errexit
# set -o nounset

# sphinxdoc-install-instance-begin
pip install psycopg2
pip install -e git+https://github.com/inveniosoftware/invenio-collections.git#egg=invenio-collections
pip install -e .
# sphinxdoc-install-instance-end

# sphinxdoc-customise-instance-begin
cdvirtualenv
mkdir -p var/${INVENIO_WEB_INSTANCE}-instance/
# sphinxdoc-customise-instance-end

# sphinxdoc-run-npm-begin
# cd ${INVENIO_WEB_INSTANCE}
${INVENIO_WEB_INSTANCE} npm
cdvirtualenv var/${INVENIO_WEB_INSTANCE}-instance/static
CI=true npm install
# cd -
# sphinxdoc-run-npm-end

# sphinxdoc-collect-and-build-assets-begin
APP_COLLECT_STORAGE=flask_collect.storage.file ${INVENIO_WEB_INSTANCE} collect -v
${INVENIO_WEB_INSTANCE} assets build
# sphinxdoc-collect-and-build-assets-end
