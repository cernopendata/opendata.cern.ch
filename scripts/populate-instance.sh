#!/usr/bin/env bash
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016, 2017 CERN.
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

${INVENIO_WEB_INSTANCE} db init
${INVENIO_WEB_INSTANCE} db create
${INVENIO_WEB_INSTANCE} index init
sleep 20

${INVENIO_WEB_INSTANCE} files location local var/data --default

${INVENIO_WEB_INSTANCE} fixtures glossary_terms
${INVENIO_WEB_INSTANCE} fixtures docs
if [[ "$@" = *"--skip-records"* ]]; then
    echo "[INFO] Skipping loading of records."
else
    if [[ "$@" = *"--skip-files"* ]]; then
        echo "[INFO] Skipping loading of record files."
        ${INVENIO_WEB_INSTANCE} fixtures records --skip-files --mode insert
    else
        # Prevent memory leak which happens when all fixtures are loaded at once
        for recordfile in $(ls -Sr cernopendata/modules/fixtures/data/records/*.json);
        do
            ${INVENIO_WEB_INSTANCE} fixtures records -f "$recordfile" --verbose --mode insert
        done
    fi
fi
