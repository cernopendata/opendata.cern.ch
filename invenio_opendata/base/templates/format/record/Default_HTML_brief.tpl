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
  {{ bfe_fulltext(bfo, show_icons="yes", prefix='<ul class="nav nav-pills pull-right" style="border-radius:0;"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" rel="tooltip" title="Download" href="#"><i class="glyphicon glyphicon-download-alt"></i><span class="caret"></span></a>', suffix='</li></ul>', focus_on_main_file="yes") }}
{% endblock %}

{% block record_header %}
  <big>
  <a href="{{ url_for('record.metadata', recid=record['recid']) }}">
    {{ record.get('title.title', '') }}
    {{- record.get('title.volume', '')|prefix(', ') }}
    {{- record.get('title.subtitle', '')|prefix(': ') }}
    {{- record.get('edition_statement', '')|prefix('; ') }}
  </a>
  </big>
{% endblock %}

{% block record_content %}
  {{ record.get('abstract.summary', '')|sentences(3) }}
  <span style="background: #ccc;"><strong>DOI:</strong> {{ record.get('doi', '') }}</span>
{% endblock %}

{% block record_info %}
  {{ record_info() }}
{% endblock %}

{% block fulltext_snippets %}
  {{ render_fulltext_snippets() }}
{% endblock %}

{% block record_footer %}
  {{ render_record_footer(4) }}
{% endblock %}