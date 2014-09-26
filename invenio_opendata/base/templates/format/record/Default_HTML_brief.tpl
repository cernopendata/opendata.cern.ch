{#
## This file is part of Invenio.
## Copyright (C) 2014 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#}

{% extends "format/record/Default_HTML_brief_base.tpl" %}

{% from "format/record/Default_HTML_brief_macros.tpl" import render_record_footer, render_fulltext_snippets, record_info with context %}

{% block above_record_header %}
  {{ bfe_fulltext(bfo, show_icons="yes", prefix='<ul class="nav nav-pills pull-right" style="margin-top: -10px;"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" rel="tooltip" title="Download" href="#"><i class="glyphicon glyphicon-download-alt"></i><span class="caret"></span></a>', suffix='</li></ul>', focus_on_main_file="yes") }}
{% endblock %}

{% block record_header %}
  <style>
  .collection-res .rec_release .t{
    color: #606D75;
    float: left;
    margin: -3px;
    padding: 3px;
    border-bottom-left-radius: 2px;
    border-top-left-radius: 2px;
    background-color: #f4f4f4;
    font-weight: 400;
    font-size: 12px;  
    text-align: left;
    margin-right: 10px;
  }
  .collection-res .rec_release .n {
    background-color: #fff;
    color: #606D75;
    float: left;
    padding: 3px;
    border-radius: 2px;
    text-align: left;
    border: 1px solid #899AA5;
    font-size: 12px;
    font-weight:400;
  }
  .collection-res .rec_thumb, 
  .collection-res .rec_title {
    float: left;
    margin-right: 10px;
  }
  .record-header, .record-content,
  .record-info {
    display: inline-block;
    width: 100%;
  }
  </style>


  <a href="{{ url_for('record.metadata', recid=record['recid']) }}">
    <div class="rec_title">{{ record.get('title.title', '') }}</div>
    {{- record.get('title.volume', '')|prefix(', ') }}
    {{- record.get('title.subtitle', '')|prefix(': ') }}
    {% if record.get('edition_statement','')  %}
    <div class="rec_thumb rec_release">
      <div class="n"><div class="t">Release</div>{{ (record.get('edition_statement')|splitthem(':'))[1] }}</div>
    </div>
    {% endif %}
  </a>
{% endblock %}

{% block record_content %}
  {{ record.get('abstract.summary', '')|sentences(3) }}
{% endblock %}

{% block fulltext_snippets %}
  {{ render_fulltext_snippets() }}
{% endblock %}

{% block record_footer %}
  {{ render_record_footer(4) }}
{% endblock %}