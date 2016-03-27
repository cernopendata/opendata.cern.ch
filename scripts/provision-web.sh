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

# sphinxdoc-install-detect-sudo-begin
# runs as root or needs sudo?
if [[ "$EUID" -ne 0 ]]; then
    sudo='sudo'
else
    sudo=''
fi
# sphinxdoc-install-detect-sudo-end

# unattended installation:
export DEBIAN_FRONTEND=noninteractive

provision_web_common_ubuntu_trusty () {

    # sphinxdoc-install-useful-system-tools-trusty-begin
    # update list of available packages:
    $sudo apt-get -y update

    # install useful system tools:
    $sudo apt-get -y install \
         curl \
         git \
         rlwrap \
         screen \
         vim
    # sphinxdoc-install-useful-system-tools-trusty-end

    # sphinxdoc-add-nodejs-external-repository-trusty-begin
    if [[ ! -f /etc/apt/sources.list.d/nodesource.list ]]; then
        curl -sL https://deb.nodesource.com/setup_4.x | $sudo bash -
    fi
    # sphinxdoc-add-nodejs-external-repository-trusty-end

    # sphinxdoc-install-web-common-trusty-begin
    $sudo apt-get -y install \
         libffi-dev \
         libfreetype6-dev \
         libjpeg-dev \
         libmsgpack-dev \
         libssl-dev \
         libtiff-dev \
         libxml2-dev \
         libxslt-dev \
         nodejs \
         python-dev \
         python-pip
    # sphinxdoc-install-web-common-trusty-end
}

provision_web_libpostgresql_ubuntu_trusty () {

    # sphinxdoc-install-web-libpostgresql-trusty-begin
    $sudo apt-get -y install \
         libpq-dev
    # sphinxdoc-install-web-libpostgresql-trusty-end
}

provision_web_common_centos7 () {

    # sphinxdoc-install-useful-system-tools-centos7-begin
    # install useful system tools:
    $sudo yum install -y \
         curl \
         git \
         rlwrap \
         screen \
         vim

    # install uuid generator (useful for loading demo records):
    $sudo yum install -y \
         uuid
    # sphinxdoc-install-useful-system-tools-centos7-end

    # sphinxdoc-add-nodejs-external-repository-centos7-begin
    # add EPEL external repository:
    $sudo yum install -y epel-release
    # sphinxdoc-add-nodejs-external-repository-centos7-end

    # sphinxdoc-install-web-common-centos7-begin
    # install development tools:
    $sudo yum update -y
    $sudo yum groupinstall -y "Development Tools"
    $sudo yum install -y \
         libffi-devel \
         libxml2-devel \
         libxslt-devel \
         npm \
         python-devel \
         python-pip
    # sphinxdoc-install-web-common-centos7-end

}

provision_web_libpostgresql_centos7 () {

    # sphinxdoc-install-web-libpostgresql-centos7-begin
    $sudo yum install -y \
         postgresql-devel
    # sphinxdoc-install-web-libpostgresql-centos7-end
}

setup_npm_and_css_js_filters () {

    # sphinxdoc-install-npm-and-css-js-filters-begin
    $sudo su -c "npm install -g npm"
    $sudo su -c "npm install -g node-sass clean-css requirejs uglify-js"
    # sphinxdoc-install-npm-and-css-js-filters-end

}

setup_virtualenvwrapper () {

    # disable quitting on errors due to virtualenvrapper:
    set +o errexit
    set +o nounset

    # sphinxdoc-install-virtualenvwrapper-begin
    $sudo pip install -U virtualenvwrapper pip
    if ! grep -q virtualenvwrapper ~/.bashrc; then
        mkdir -p $HOME/.virtualenvs
        echo "export WORKON_HOME=$HOME/.virtualenvs" >> $HOME/.bashrc
        echo "source $(which virtualenvwrapper.sh)" >> $HOME/.bashrc
    fi
    export WORKON_HOME=$HOME/.virtualenvs
    source $(which virtualenvwrapper.sh)
    # sphinxdoc-install-virtualenvwrapper-end

    # enable quitting on errors back:
    set -o errexit
    set -o nounset

}

cleanup_web_ubuntu_trusty () {
    # sphinxdoc-install-web-cleanup-trusty-begin
    $sudo apt-get -y autoremove && $sudo apt-get -y clean
    # sphinxdoc-install-web-cleanup-trusty-end
}

cleanup_web_centos7 () {
    # sphinxdoc-install-web-cleanup-centos7-begin
    $sudo yum clean -y all
    # sphinxdoc-install-web-cleanup-centos7-end
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
    if [ -f /.dockerinit ]; then
        # running inside Docker
        provision_web_common_ubuntu_trusty
        provision_web_libpostgresql_ubuntu_trusty
        setup_npm_and_css_js_filters
        setup_virtualenvwrapper
        cleanup_web_ubuntu_trusty
    elif [ "$os_distribution" = "Ubuntu" ]; then
        if [ "$os_release" = "14.04" ]; then
            provision_web_common_ubuntu_trusty
            provision_web_libpostgresql_ubuntu_trusty
            setup_npm_and_css_js_filters
            setup_virtualenvwrapper
            cleanup_web_ubuntu_trusty
        else
            echo "[ERROR] Sorry, unsupported release ${os_release}."
            exit 1
        fi
    elif [ "$os_distribution" = "CentOS" ]; then
        if [ "$os_release" = "7" ]; then
            provision_web_common_centos7
            provision_web_libpostgresql_centos7
            setup_npm_and_css_js_filters
            setup_virtualenvwrapper
            cleanup_web_centos7
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
