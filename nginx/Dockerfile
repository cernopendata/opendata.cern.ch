# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2016, 2022, 2023 CERN.
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

FROM docker.io/library/nginx:1.22-perl

RUN rm /etc/nginx/conf.d/default.conf
COPY localhost.conf /etc/nginx/conf.d/
COPY localhost.crt /etc/ssl/localhost.crt
COPY localhost.key /etc/ssl/localhost.key

# Need to include perl-module because of uri lowercasing implementation
CMD ["nginx", "-g", "daemon off; load_module /etc/nginx/modules/ngx_http_perl_module.so;"]
