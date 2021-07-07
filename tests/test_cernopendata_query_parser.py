# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2021 CERN.
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

"""cernopendata-query-parser test."""

from elasticsearch_dsl.query import Bool, Match, QueryString

from cernopendata.modules.records.search.query import cernopendata_query_parser


def test_cernopendata_query_parser():
    assert cernopendata_query_parser('/Btau') == Bool(must=[QueryString(query='"/Btau"')], must_not=[Match(distribution__availability__keyword='ondemand')])
    assert cernopendata_query_parser('"/Btau"') == Bool(must=[QueryString(query='"/Btau"')], must_not=[Match(distribution__availability__keyword='ondemand')])
    assert cernopendata_query_parser('/btau AND CMS') == Bool(must=[QueryString(query='"/btau" AND CMS')], must_not=[Match(distribution__availability__keyword='ondemand')])
    assert cernopendata_query_parser('"/btau" AND CMS') == Bool(must=[QueryString(query='"/btau" AND CMS')], must_not=[Match(distribution__availability__keyword='ondemand')])
    assert cernopendata_query_parser('CMS AND /btau') == Bool(must=[QueryString(query='CMS AND "/btau"')], must_not=[Match(distribution__availability__keyword='ondemand')])
    assert cernopendata_query_parser('CMS AND /btau', show_ondemand='true') == QueryString(query='CMS AND "/btau"')
