#!/usr/bin/env bash
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2015, 2016, 2017, 2018, 2019, 2020, 2024 CERN.
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

check_script () {
    shellcheck run-tests.sh
}

check_black () {
    black --check .
}


check_fixtures () {
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
    # shellcheck disable=SC2044
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
    # shellcheck disable=SC2044
    for file in $(find cernopendata/modules/fixtures/data/{records,docs}/ -name "*.json"); do
        secondaries=$(jq '.[].type.secondary' "$file" -c | sort | uniq)
        if echo "$secondaries" | grep -q -e '\[\]' -e "null"; then
            echo "[Warning] empty type.secondary field in $file"
        fi
    done
}

check_pycodestyle () {
    pycodestyle --max-line-length=120 cernopendata
}

check_pydocstyle () {
    pydocstyle cernopendata
}

check_isort () {
    isort -rc -c -df --profile black -- **/*.py
}

check_manifest () {
    check-manifest --ignore "*.crt,*.key,.htpasswd"
}

check_docker_build () {
    docker compose build
}

check_pytest () {
    python setup.py test
}

check_all () {
    check_script
    check_fixtures
    check_pycodestyle
    check_black
    check_pydocstyle
    check_isort
    check_manifest
    check_docker_build
    check_pytest
}

if [ $# -eq 0 ]; then
    check_all
    exit 0
fi

for arg in "$@"
do
    case $arg in
        --check-shellscript) check_script;;
        --check-fixtures) check_fixtures;;
        --check-pycodestyle) check_pycodestyle;;
        --check-pydocstyle) check_pydocstyle;;
        --check-isort) check_isort;;
        --check-manifest) check_manifest;;
        --check-docker-build) check_docker_build;;
        --check-pytest) check_pytest;;
        *)
    esac
done
