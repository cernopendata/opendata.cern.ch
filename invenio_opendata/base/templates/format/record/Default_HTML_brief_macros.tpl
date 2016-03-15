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

{% macro render_record_footer(number_of_displayed_authors) %} 
      <a href="{{url_for('search.search', cc=record['collections'][0]['primary'] )}}">
        <div class="rec_thumb_brief rec_footer_thumb rec_collection pull-ight">
          <div class="n no-glossary">
            <div class="t">Collection</div>
            {{ record['collections'][0]['primary'] }}
          </div>
        </div>
      </a>
      {% if record.get('number_of_authors', 0) > 0 %}
        {% set authors = record.get('authors[:].full_name', []) %}
        {% set sep = joiner('<i style="float:left;padding-right:3px;"> ; </i>') %}
        <div class="rec_thumb_brief rec_footer_thumb">
          <div class="n no-glossary">
            <div class="t">Author</div>
            {% for full_name in authors[0:number_of_displayed_authors] %} {{ sep() }}
              <a href="{{ url_for('search.search', p='author:"' + full_name + '"') }}">{{ full_name }}</a>
            {% endfor %}
            {% if record.get('number_of_authors', 0) > number_of_displayed_authors %}
            {{ sep() }}
            <a href="#authors_{{ record['recid'] }}"
            class="text-muted" data-toggle="modal"
            data-target="#authors_{{ record['recid'] }}">
            <em>{{ _(' et al') }}</em>
            </a>
            {% endif %}
          </div>
        </div>
      {% endif %}
      {% if record.get('doi','') %}
      <a href="{{ url_for('record.metadata', recid=record['recid']) }}">
        <div class="rec_thumb_brief rec_footer_thumb pull-right">
          <div class="n no-glossary"><div class="t">DOI</div>{{ record.get('doi', '') }}</div>
        </div>
      </a>
      {% endif %}
      {% if record.get('supplement_parent_entry','') %}
        {% if record.get('supplement_parent_entry','').get('recid','') and record.get('supplement_parent_entry','').get('heading','') %}
        <a href="{{ url_for('record.metadata', recid=record.get('supplement_parent_entry','').get('recid', '')) }}">
          <div class="rec_thumb_brief rec_footer_thumb pull-right ">
            <div class="n no-glossary"><div class="t">Parent Dataset</div>{{ record.get('supplement_parent_entry','').get('heading', '') }}</div>
          </div>
        </a> 
        {% endif %}
      {% endif %}
{% endmacro %}

{% macro render_fulltext_snippets() %}
  {{ tfn_get_fulltext_snippets(record['recid'], request.args['p'], qid, current_user) | wrap(prefix='<p><small>', suffix='</small></p>') }}
{% endmacro %}

{% macro record_info() %}
  {{ record.get('primary_report_number')|prefix('<i class="glyphicon glyphicon-qrcode"></i> ') }}
  {{ bfe_additional_report_numbers(bfo, prefix='<i class="glyphicon glyphicon-qrcode"></i> ',
                                   separator=' <i class="glyphicon glyphicon-qrcode"></i> ') }}

  {{ bfe_publi_info(bfo, prefix='| <i class="glyphicon glyphicon-book"></i> ') }}
  {{ bfe_doi(bfo, prefix='| <i class="glyphicon glyphicon-barcode"></i> ') }}
  {# '<a href="http://dx.doi.org/%(doi)s" title="DOI" target="_blank"><i class="glyphicon glyphicon-barcode"></i> %(doi)s</a>'|format(doi=record['doi']) if record.get('doi') #}

{% endmacro %}
