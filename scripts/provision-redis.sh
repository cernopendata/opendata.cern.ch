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

# check environment variables:
if [ -v ${INVENIO_REDIS_HOST} ]; then
    echo "[ERROR] Please set environment variable INVENIO_REDIS_HOST before runnning this script."
    echo "[ERROR] Example: export INVENIO_REDIS_HOST=192.168.50.12"
    exit 1
fi

# quit on unbound symbols:
set -o nounset

provision_redis_ubuntu_trusty () {

    # sphinxdoc-install-redis-trusty-begin
    # update list of available packages:
    sudo DEBIAN_FRONTEND=noninteractive apt-get -y update

    # install Redis server:
    sudo DEBIAN_FRONTEND=noninteractive apt-get -y install \
         redis-server

    # allow network connections:
    if ! grep -q ${INVENIO_REDIS_HOST} /etc/redis/redis.conf; then
        sudo sed -i "s/bind 127.0.0.1/bind 127.0.0.1 ${INVENIO_REDIS_HOST}/" \
             /etc/redis/redis.conf
    fi

    # restart Redis server:
    sudo /etc/init.d/redis-server restart
    # sphinxdoc-install-redis-trusty-end

}

provision_redis_centos7 () {

    # sphinxdoc-install-redis-centos7-begin
    # add EPEL external repository:
    sudo yum install -y epel-release

    # update list of available packages:
    sudo yum update -y

    # install Redis server:
    sudo yum install -y \
         redis

    # allow network connections:
    if ! grep -q ${INVENIO_REDIS_HOST} /etc/redis.conf; then
        sudo sed -i "s/bind 127.0.0.1/bind 127.0.0.1 ${INVENIO_REDIS_HOST}/" \
             /etc/redis.conf
    fi

    # open firewall ports:
    if firewall-cmd --state | grep -q running; then
        sudo firewall-cmd --zone=public --add-port=6379/tcp --permanent
        sudo firewall-cmd --reload
    fi

    # enable Redis upon reboot:
    sudo systemctl enable redis

    # start Redis:
    sudo systemctl start redis
    # sphinxdoc-install-redis-centos7-end

}

cleanup_redis_ubuntu_trusty () {
    # sphinxdoc-install-redis-cleanup-trusty-begin
    sudo apt-get -y autoremove && sudo apt-get -y clean
    # sphinxdoc-install-redis-cleanup-trusty-end
}

cleanup_redis_centos7 () {
    # sphinxdoc-install-redis-cleanup-centos7-begin
    sudo yum clean -y all
    # sphinxdoc-install-redis-cleanup-centos7-end
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
            provision_redis_ubuntu_trusty
            cleanup_redis_ubuntu_trusty
        else
            echo "[ERROR] Sorry, unsupported release ${os_release}."
            exit 1
        fi
    elif [ "$os_distribution" = "CentOS" ]; then
        if [ "$os_release" = "7" ]; then
            provision_redis_centos7
            cleanup_redis_centos7
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
