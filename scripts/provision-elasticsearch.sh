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

# runs as root or needs sudo?
if [[ "$EUID" -ne 0 ]]; then
  sudo='sudo'
else
  sudo=''
fi

check_environment_variables () {
    # check environment variables:
    if [ -v ${INVENIO_ELASTICSEARCH_HOST} ]; then
        echo "[ERROR] Please set environment variable INVENIO_ELASTICSEARCH_HOST before runnning this script."
        echo "[ERROR] Example: export INVENIO_ELASTICSEARCH_HOST=192.168.50.12"
        exit 1
    fi
}

# quit on unbound symbols:
set -o nounset

provision_elasticsearch_ubuntu14 () {

    # sphinxdoc-install-elasticsearch-ubuntu14-begin
    # install curl:
    sudo apt-get -y install curl

    # add external Elasticsearch repository:
    if [[ ! -f /etc/apt/sources.list.d/elasticsearch-2.x.list ]]; then
        curl -sL https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
        echo "deb http://packages.elastic.co/elasticsearch/2.x/debian stable main" | \
            sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list
    fi

    # update list of available packages:
    sudo DEBIAN_FRONTEND=noninteractive apt-get -y update

    # install Elasticsearch server:
    sudo DEBIAN_FRONTEND=noninteractive apt-get -y install \
         elasticsearch \
         openjdk-7-jre

    # allow network connections:
    if ! sudo grep -q "network.host: ${INVENIO_ELASTICSEARCH_HOST}" \
         /etc/elasticsearch/elasticsearch.yml; then
        echo "network.host: ${INVENIO_ELASTICSEARCH_HOST}" | \
            sudo tee -a /etc/elasticsearch/elasticsearch.yml
    fi

    # enable Elasticsearch upon reboot:
    sudo update-rc.d elasticsearch defaults 95 10

    # start Elasticsearch:
    sudo /etc/init.d/elasticsearch restart
    # sphinxdoc-install-elasticsearch-ubuntu14-end

}

provision_elasticsearch_centos7 () {

    # sphinxdoc-install-elasticsearch-centos7-begin
    # add external Elasticsearch repository:
    if [[ ! -f /etc/yum.repos.d/elasticsearch.repo ]]; then
        sudo rpm --import \
             https://packages.elastic.co/GPG-KEY-elasticsearch
        echo "[elasticsearch-2.x]
name=Elasticsearch repository for 2.x packages
baseurl=http://packages.elastic.co/elasticsearch/2.x/centos
gpgcheck=1
gpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch
enabled=1" | \
            sudo tee -a /etc/yum.repos.d/elasticsearch.repo
    fi

    # update list of available packages:
    sudo yum update -y

    # install Elasticsearch:
    sudo yum install -y \
         elasticsearch \
         java

    # allow network connections:
    if ! sudo grep -q "network.host: ${INVENIO_ELASTICSEARCH_HOST}" \
         /etc/elasticsearch/elasticsearch.yml; then
        echo "network.host: ${INVENIO_ELASTICSEARCH_HOST}" | \
            sudo tee -a /etc/elasticsearch/elasticsearch.yml
    fi

    # open firewall ports:
    if firewall-cmd --state | grep -q running; then
        sudo firewall-cmd --zone=public --add-port=9200/tcp --permanent
        sudo firewall-cmd --reload
    fi

    # enable Elasticsearch upon reboot:
    sudo systemctl enable elasticsearch

    # start Elasticsearch:
    sudo systemctl start elasticsearch
    # sphinxdoc-install-elasticsearch-centos7-end

}

install_plugins () {
    # sphinxdoc-install-elasticsearch-plugins-begin
    $sudo /usr/share/elasticsearch/bin/plugin install -b mapper-attachments
    # sphinxdoc-install-elasticsearch-plugins-end
}

cleanup_elasticsearch_ubuntu14 () {
    # sphinxdoc-install-elasticsearch-cleanup-ubuntu14-begin
    sudo apt-get -y autoremove && sudo apt-get -y clean
    # sphinxdoc-install-elasticsearch-cleanup-ubuntu14-end
}

cleanup_elasticsearch_centos7 () {
    # sphinxdoc-install-elasticsearch-cleanup-centos7-begin
    sudo yum clean -y all
    # sphinxdoc-install-elasticsearch-cleanup-centos7-end
}

main () {

    # detect OS distribution and release version:
    if hash lsb_release 2> /dev/null; then
        os_distribution=$(lsb_release -i | cut -f 2)
        os_release=$(lsb_release -r | cut -f 2 | grep -oE '[0-9]+\.' | cut -d. -f1 | head -1)
    elif [ -e /etc/redhat-release ]; then
        os_distribution=$(cut -d ' ' -f 1 /etc/redhat-release)
        os_release=$(grep -oE '[0-9]+\.' /etc/redhat-release | cut -d. -f1 | head -1)
    elif [ -f /.dockerinit -o -f /.dockerenv ]; then
        # running inside Docker
        os_distribution="Docker"
        os_release=""
    else
        os_distribution="UNDETECTED"
        os_release="UNDETECTED"
    fi

    # call appropriate provisioning functions:
    if [ "$os_distribution" = "Ubuntu" ]; then
        if [ "$os_release" = "14" ]; then
            check_environment_variables
            provision_elasticsearch_ubuntu14
            install_plugins
        else
            echo "[ERROR] Sorry, unsupported release ${os_release}."
            exit 1
        fi
    elif [ "$os_distribution" = "CentOS" ]; then
        if [ "$os_release" = "7" ]; then
            check_environment_variables
            provision_elasticsearch_centos7
            install_plugins
        else
            echo "[ERROR] Sorry, unsupported release ${os_release}."
            exit 1
        fi
    elif [ "$os_distribution" = "Docker" ]; then
        install_plugins
    else
        echo "[ERROR] Sorry, unsupported distribution ${os_distribution}."
        exit 1
    fi

}

main
