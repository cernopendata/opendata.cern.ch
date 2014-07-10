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

{% extends "format/record/Default_HTML_detailed_base.tpl" %}

{% block header %}
    {{ bfe_topbanner(bfo, prefix='<div style="padding-left:10px;padding-right:10px">', suffix='</div><hr/>') }}
    <h1>
    {{ bfe_title(bfo, separator="<br /><br />") }}
    </h1>
{% endblock %}
OB
{% block details %}
    <big>
    {{ bfe_authors(bfo, suffix="<br />", limit="25", interactive="yes", print_affiliations="yes", affiliation_prefix="<small> (", affiliation_suffix=")</small>") }}
    </big>
    {{ bfe_addresses(bfo) }}
    {{ bfe_affiliation(bfo) }}
    {{ bfe_date(bfo, prefix="<br />", suffix="<br />") }}
    {{ bfe_publisher(bfo, prefix="<small>", suffix="</small>") }}
    {{ bfe_place(bfo, prefix="<small>", suffix="</small>") }}
    {{ bfe_isbn(bfo, prefix="<br />ISBN: ") }}
{% endblock %}

{% block abstract %}
    {{ bfe_abstract(bfo, prefix_en="<small><strong>Abstract: </strong>", prefix_fr="<small><strong>Résumé: </strong>", suffix_en="</small><br />", suffix_fr="</small><br />") }}

    {{ bfe_keywords(bfo, prefix="<br /><small><strong>Keyword(s): </strong></small>", keyword_prefix="<small>", keyword_suffix="</small>") }}

    {{ bfe_notes(bfo, note_prefix="<br />", note_suffix="", suffix="<br />") }}

    {{ bfe_publi_info(bfo, prefix="<br /><br /><strong>Published in: </strong>") }}<br />
    {{ bfe_doi(bfo, tag="0247_", prefix='<span style="background: #ccc;"><strong>DOI: </strong>', suffix=" </span><br />") }}

    {{ bfe_plots(bfo, width="200px", caption="no") }}

{% if record['recid'] == 15 %}
   <center>
   <img src="{{ url_for("static", filename="img/cms-d3-visualisation.png")}}" alt=""/>
   </center>
{% endif %}

{% endblock %}

{% block footer %}
    {# WebTags #}
    {{ tfn_webtag_record_tags(record['recid'], current_user.get_id())|prefix('<hr />') }}

    {{ tfn_get_back_to_search_links(record['recid'])|wrap(prefix='<div class="pull-right linksbox">', suffix='</div>') }}
{% endblock %}
