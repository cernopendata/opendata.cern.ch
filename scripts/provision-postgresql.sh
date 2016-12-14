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
if [ -v ${INVENIO_POSTGRESQL_HOST} ]; then
    echo "[ERROR] Please set environment variable INVENIO_POSTGRESQL_HOST before runnning this script."
    echo "[ERROR] Example: export INVENIO_POSTGRESQL_HOST=192.168.50.11"
    exit 1
fi
if [ -v ${INVENIO_POSTGRESQL_DBNAME} ]; then
    echo "[ERROR] Please set environment variable INVENIO_POSTGRESQL_DBNAME before runnning this script."
    echo "[ERROR] Example: INVENIO_POSTGRESQL_DBNAME=invenio3"
    exit 1
fi
if [ -v ${INVENIO_POSTGRESQL_DBUSER} ]; then
    echo "[ERROR] Please set environment variable INVENIO_POSTGRESQL_DBUSER before runnning this script."
    echo "[ERROR] Example: INVENIO_POSTGRESQL_DBUSER=invenio3"
    exit 1
fi
if [ -v ${INVENIO_POSTGRESQL_DBPASS} ]; then
    echo "[ERROR] Please set environment variable INVENIO_POSTGRESQL_DBPASS before runnning this script."
    echo "[ERROR] Example: INVENIO_POSTGRESQL_DBPASS=dbpass123"
    exit 1
fi
if [ -v ${INVENIO_WEB_HOST} ]; then
    echo "[ERROR] Please set environment variable INVENIO_WEB_HOST before runnning this script."
    echo "[ERROR] Example: export INVENIO_WEB_HOST=192.168.50.10"
    exit 1
fi

# quit on unbound symbols:
set -o nounset

provision_postgresql_ubuntu14 () {

    # sphinxdoc-install-postgresql-ubuntu14-begin
    # update list of available packages:
    sudo DEBIAN_FRONTEND=noninteractive apt-get -y update

    # install PostgreSQL:
    sudo DEBIAN_FRONTEND=noninteractive apt-get -y install \
         postgresql

    # allow network connections:
    if ! grep -q listen_addresses.*${INVENIO_POSTGRESQL_HOST} \
         /etc/postgresql/9.3/main/postgresql.conf; then
        echo "listen_addresses = '${INVENIO_POSTGRESQL_HOST}'" | \
            sudo tee -a /etc/postgresql/9.3/main/postgresql.conf
    fi

    # grant access rights:
    if ! sudo grep -q host.*${INVENIO_POSTGRESQL_DBNAME}.*${INVENIO_POSTGRESQL_DBUSER} \
         /etc/postgresql/9.3/main/pg_hba.conf; then
        echo "host ${INVENIO_POSTGRESQL_DBNAME} ${INVENIO_POSTGRESQL_DBUSER} ${INVENIO_WEB_HOST}/32 md5" | \
            sudo tee -a /etc/postgresql/9.3/main/pg_hba.conf
    fi

    # grant database creation rights via SQLAlchemy-Utils:
    if ! sudo grep -q host.*template1.*${INVENIO_POSTGRESQL_DBUSER} \
         /etc/postgresql/9.3/main/pg_hba.conf; then
        echo "host template1 ${INVENIO_POSTGRESQL_DBUSER} ${INVENIO_WEB_HOST}/32 md5" | \
            sudo tee -a /etc/postgresql/9.3/main/pg_hba.conf
    fi

    # restart PostgreSQL server:
    sudo /etc/init.d/postgresql restart
    # sphinxdoc-install-postgresql-ubuntu14-end

}

provision_postgresql_centos7 () {

    # sphinxdoc-install-postgresql-centos7-begin
    # add EPEL external repository:
    sudo yum install -y epel-release

    # install PostgreSQL:
    sudo yum update -y
    sudo yum install -y \
         postgresql-server

    # initialise PostgreSQL database:
    sudo -i -u postgres pg_ctl initdb

    # allow network connections:
    if ! sudo grep -q listen_addresses.*${INVENIO_POSTGRESQL_HOST} \
         /var/lib/pgsql/data/postgresql.conf; then
        echo "listen_addresses = '${INVENIO_POSTGRESQL_HOST}'" | \
            sudo tee -a /var/lib/pgsql/data/postgresql.conf
    fi

    # grant access rights:
    if ! sudo grep -q host.*${INVENIO_POSTGRESQL_DBNAME}.*${INVENIO_POSTGRESQL_DBUSER} \
         /var/lib/pgsql/data/pg_hba.conf; then
        echo "host ${INVENIO_POSTGRESQL_DBNAME} ${INVENIO_POSTGRESQL_DBUSER} ${INVENIO_WEB_HOST}/32 md5" | \
            sudo tee -a /var/lib/pgsql/data/pg_hba.conf
    fi

    # grant database creation rights via SQLAlchemy-Utils:
    if ! sudo grep -q host.*template1.*${INVENIO_POSTGRESQL_DBUSER} \
         /var/lib/pgsql/data/pg_hba.conf; then
        echo "host template1 ${INVENIO_POSTGRESQL_DBUSER} ${INVENIO_WEB_HOST}/32 md5" | \
            sudo tee -a /var/lib/pgsql/data/pg_hba.conf
    fi

    # open firewall ports:
    if firewall-cmd --state | grep -q running; then
        sudo firewall-cmd --zone=public --add-service=postgresql --permanent
        sudo firewall-cmd --reload
    fi

    # enable PostgreSQL upon reboot:
    sudo systemctl enable postgresql

    # restart PostgreSQL server:
    sudo systemctl start postgresql
    # sphinxdoc-install-postgresql-centos7-end

}

cleanup_postgresql_ubuntu14 () {
    # sphinxdoc-install-postgresql-cleanup-ubuntu14-begin
    sudo apt-get -y autoremove && sudo apt-get -y clean
    # sphinxdoc-install-postgresql-cleanup-ubuntu14-end
}

cleanup_postgresql_centos7 () {
    # sphinxdoc-install-postgresql-cleanup-centos7-begin
    sudo yum clean -y all
    # sphinxdoc-install-postgresql-cleanup-centos7-end
}

setup_db () {

    # sphinxdoc-setup-postgresql-access-begin
    # create user if it does not exist:
    echo "SELECT 1 FROM pg_roles WHERE rolname='${INVENIO_POSTGRESQL_DBUSER}'" | \
        sudo -i -u postgres psql -tA | grep -q 1 || \
        echo "CREATE USER ${INVENIO_POSTGRESQL_DBUSER} WITH PASSWORD '${INVENIO_POSTGRESQL_DBPASS}';" | \
            sudo -i -u postgres psql

    # create database if it does not exist:
    echo "SELECT 1 FROM pg_database WHERE datname='${INVENIO_POSTGRESQL_DBNAME}'" | \
        sudo -i -u postgres psql -tA | grep -q 1 || \
        echo "CREATE DATABASE ${INVENIO_POSTGRESQL_DBNAME};" | \
            sudo -i -u postgres psql

    # grant privileges to the user on this database:
    echo "GRANT ALL PRIVILEGES ON DATABASE ${INVENIO_POSTGRESQL_DBNAME} TO ${INVENIO_POSTGRESQL_DBUSER};" | \
        sudo -i -u postgres psql
    # sphinxdoc-setup-postgresql-access-end
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
            provision_postgresql_ubuntu14
        else
            echo "[ERROR] Sorry, unsupported release ${os_release}."
            exit 1
        fi
    elif [ "$os_distribution" = "CentOS" ]; then
        if [ "$os_release" = "7" ]; then
            provision_postgresql_centos7
        else
            echo "[ERROR] Sorry, unsupported release ${os_release}."
            exit 1
        fi
    else
        echo "[ERROR] Sorry, unsupported distribution ${os_distribution}."
        exit 1
    fi

    # finish with common setups:
    setup_db

}

main
