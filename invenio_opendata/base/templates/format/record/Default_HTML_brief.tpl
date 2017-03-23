{#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2014 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#}

{% extends "format/record/Default_HTML_brief_base.tpl" %}

{% from "format/record/Default_HTML_brief_macros.tpl" import render_record_footer, render_fulltext_snippets, record_info with context %}

{% block above_record_header %}
  {{ bfe_fulltext(bfo, show_icons="yes", prefix='<ul class="nav nav-pills pull-right" style="margin-top: -10px;"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" rel="tooltip" title="Download" href="#"><i class="glyphicon glyphicon-download-alt"></i><span class="caret"></span></a>', suffix='</li></ul>', focus_on_main_file="yes") }}
{% endblock %}

{% block record_header %}
  <a href="{{ url_for('record.metadata', recid=record['recid']) }}" alt="{{ record.get('title.title', '') }}">
    <div class="no-glossary rec_title">{{ record.get('title.title', '') }}</div>
    {{- record.get('title.volume', '')|prefix(', ') }}
    {{- record.get('title.subtitle', '')|prefix(': ') }}
  </a>
{% endblock %}

{% block record_content %}
  {% if record.get('abstract.summary', '') %}
    {{ record.get('abstract.summary', '')|sentences(3) }}
  {% else %}
    {{ _('Description is not provided') }}
  {% endif %}

{% endblock %}

{% block fulltext_snippets %}
  {{ render_fulltext_snippets() }}
{% endblock %}

{% block record_footer %}
  <div class="record-footer">
    {{ render_record_footer(4) }}
  </div>
{% endblock %}

{% block record_details %}
  {% if record.get('edition_statement','') %}
    {% if record.get('edition_statement', '').get('statement', '') %}
      {% set pp = record.get('edition_statement', '').get('statement', '').replace('Release: ', '') %}
      <a href="{{url_for('search.search', p=pp) }}">
        <div class="rec_thumb_brief rec_footer_thumb  rec_release pull-right">
          <div class="n no-glossary"><div class="t">Release</div>{{ pp }}</div>
        </div>
      </a> 
    {% endif %}
    {% if record.get('edition_statement', '').get('remainder', '') %}
      {% set rr = record.get('edition_statement', '').get('remainder', '').replace('Global tag: ', '') %}
      <a href="{{ url_for('search.search', p=rr) }}">
        <div class="rec_thumb_brief rec_footer_thumb  rec_release pull-right">
          <div class="n no-glossary"><div class="t">Global tag</div>{{ rr }}</div>
        </div>
      </a> 
    {% endif %}
  {% endif %}
{% endblock %}
