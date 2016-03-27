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

# quit on errors:
set -o errexit

# quit on unbound symbols:
set -o nounset

provision_worker_ubuntu_trusty () {

    # sphinxdoc-install-worker-trusty-begin
    echo "FIXME worker is a copy of web node"
    # sphinxdoc-install-worker-trusty-end

}

provision_worker_centos7 () {

    # sphinxdoc-install-worker-centos7-begin
    echo "FIXME worker is a copy of web node"
    # sphinxdoc-install-worker-centos7-end

}

cleanup_worker_ubuntu_trusty () {
    # sphinxdoc-install-worker-cleanup-trusty-begin
    sudo apt-get -y autoremove && sudo apt-get -y clean
    # sphinxdoc-install-worker-cleanup-trusty-end
}

cleanup_worker_centos7 () {
    # sphinxdoc-install-worker-cleanup-centos7-begin
    sudo yum clean -y all
    # sphinxdoc-install-worker-cleanup-centos7-end
}

main () {

    # detect OS distribution and release version:
    if hash lsb_release 2> /dev/null; then
        os_distribution=$(lsb_release -i | cut -f 2)
        os_release=$(lsb_release -r | cut -f 2)
    elif [ -e /etc/redhat-release ]; then
        os_distribution=$(cat /etc/redhat-release | cut -d ' ' -f 1)
        os_release=$(cat /etc/redhat-release | grep -oE '[0-9]+\.' | cut -d. -f1 | head -1)
    else
        os_distribution="UNDETECTED"
        os_release="UNDETECTED"
    fi

    # call appropriate provisioning functions:
    if [ "$os_distribution" = "Ubuntu" ]; then
        if [ "$os_release" = "14.04" ]; then
            provision_worker_ubuntu_trusty
            cleanup_worker_ubuntu_trusty
        else
            echo "[ERROR] Sorry, unsupported release ${os_release}."
            exit 1
        fi
    elif [ "$os_distribution" = "CentOS" ]; then
        if [ "$os_release" = "7" ]; then
            provision_worker_centos7
            cleanup_worker_centos7
        else
            echo "[ERROR] Sorry, unsupported release ${os_release}."
            exit 1
        fi
    else
        echo "[ERROR] Sorry, unsupported distribution ${os_distribution}."
        exit 1
    fi

}

main
