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

provision_rabbitmq_ubuntu14 () {

    # sphinxdoc-install-rabbitmq-ubuntu14-begin
    # update list of available packages:
    sudo DEBIAN_FRONTEND=noninteractive apt-get -y update

    # install RabbitMQ server:
    sudo DEBIAN_FRONTEND=noninteractive apt-get -y install \
         rabbitmq-server
    # sphinxdoc-install-rabbitmq-ubuntu14-end

}

provision_rabbitmq_centos7 () {

    # sphinxdoc-install-rabbitmq-centos7-begin
    # add EPEL external repository:
    sudo yum install -y epel-release

    # update list of available packages:
    sudo yum update -y

    # install Rabbitmq:
    sudo yum install -y \
         rabbitmq-server

    # open firewall ports:
    if firewall-cmd --state | grep -q running; then
        sudo firewall-cmd --zone=public --add-port=5672/tcp --permanent
        sudo firewall-cmd --reload
    fi

    # enable RabbitMQ upon reboot:
    sudo systemctl enable rabbitmq-server

    # start RabbitMQ:
    sudo systemctl start rabbitmq-server
    # sphinxdoc-install-rabbitmq-centos7-end

}

setup_firewall_redis_centos7 () {

    # sphinxdoc-setup-firewall-redis-centos7-begin
    if firewall-cmd --state | grep -q running; then
        sudo firewall-cmd --zone=public --add-port=6379/tcp --permanent
        sudo firewall-cmd --reload
    fi
    # sphinxdoc-setup-firewall-redis-centos7-end
}

cleanup_rabbitmq_ubuntu14 () {
    # sphinxdoc-install-rabbitmq-cleanup-ubuntu14-begin
    sudo apt-get -y autoremove && sudo apt-get -y clean
    # sphinxdoc-install-rabbitmq-cleanup-ubuntu14-end
}

cleanup_rabbitmq_centos7 () {
    # sphinxdoc-install-rabbitmq-cleanup-centos7-begin
    sudo yum clean -y all
    # sphinxdoc-install-rabbitmq-cleanup-centos7-end
}

main () {

    # detect OS distribution and release version:
    if hash lsb_release 2> /dev/null; then
        os_distribution=$(lsb_release -i | cut -f 2)
        os_release=$(lsb_release -r | cut -f 2 | grep -oE '[0-9]+\.' | cut -d. -f1 | head -1)
    elif [ -e /etc/redhat-release ]; then
        os_distribution=$(cut -d ' ' -f 1 /etc/redhat-release)
        os_release=$(grep -oE '[0-9]+\.' /etc/redhat-release | cut -d. -f1 | head -1)
    else
        os_distribution="UNDETECTED"
        os_release="UNDETECTED"
    fi

    # call appropriate provisioning functions:
    if [ "$os_distribution" = "Ubuntu" ]; then
        if [ "$os_release" = "14" ]; then
            provision_rabbitmq_ubuntu14
        else
            echo "[ERROR] Sorry, unsupported release ${os_release}."
            exit 1
        fi
    elif [ "$os_distribution" = "CentOS" ]; then
        if [ "$os_release" = "7" ]; then
            provision_rabbitmq_centos7
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
