#!/usr/bin/env bash
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2015, 2016, 2017, 2018 CERN.
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

# quit on errors and potentially unbound symbols:
set -o errexit
set -o nounset

# check for possibly incorrect JSON files:
find cernopendata/modules/fixtures/data/ -name "*.json" -exec jsonlint -q {} \;

# check record ID uniqueness:
dupes=$(jq '.[].recid' cernopendata/modules/fixtures/data/records/*.json | sort | uniq -d)
if [ "x${dupes}" != "x" ]; then
    echo "[ERROR] Found duplicate record IDs:"
    echo "${dupes}"
    exit 1
fi

# check DOI uniqueness:
dupes=$(jq '.[].doi' cernopendata/modules/fixtures/data/records/*.json | sort | grep -v null | uniq -d)
if [ "x${dupes}" != "x" ]; then
    echo "[ERROR] Found duplicate record DOIs:"
    echo "${dupes}"
    exit 1
fi

# check docs slug uniqueness:
dupes=$(for file in $(find cernopendata/modules/fixtures/data/docs -name "*.json"); do jq '.[].slug' "$file"; done | sort | grep -v null | uniq -d)
if [ "x${dupes}" != "x" ]; then
    echo "[ERROR] Found duplicate docs slugs:"
    echo "${dupes}"
    exit 1
fi

# check trailing whitespace:
whitespace_found_p=0
for file in $(git ls-files | grep -E '.(py|html|css|json|md|sh|txt|yml)$'); do
    if grep -q ' $' "$file"; then
        whitespace_found_p=1
        echo "[ERROR] Found trailing whitespace in ${file}."
    fi
done
if [ "${whitespace_found_p}" != "0" ]; then
    exit 1
fi

# check for empty secondary type in fixtures
for file in $(find cernopendata/modules/fixtures/data/{records,docs}/ -name "*.json"); do
    secondaries=$(jq '.[].type.secondary' $file -c | sort | uniq)
    if echo $secondaries | grep -q -e '\[\]' -e "null"; then
        echo "[Warning] empty type.secondary field in $file"
    fi
done

# do we need to continue?
if [[ "$@" = *"--check-fixtures-only"* ]]; then
    exit 0
fi

# check source code style:
pycodestyle cernopendata
pydocstyle cernopendata
isort -rc -c -df **/*.py
check-manifest --ignore ".travis-*"

# check our test suite:
python setup.py test
