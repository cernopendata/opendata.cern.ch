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
<h4 class="record-header col-xs-12 no-padding">
  {% block record_header %}
  {% endblock %} 
</h4>
<div class="record-brief-main col-xs-12 col-sm-8 no-padding">
{% block record_main %}
<div class="record-brief">  
  
  <div class="record-content">

    <span class="pull-left record-leftside">
      {% block record_media %}
      {% endblock %}
    </span>

    <p class="record-abstract">
      {% block record_content %}
      {% endblock %}
    </p>
  </div>

  {% block fulltext_snippets %}
  {% endblock %}

  {% block record_footer %}
  {% endblock %}
</div>
{% endblock %}
</div>
<div class="record-brief-details col-sm-4 col-xs-12 no-padding">
  {% block record_details %}
  {% endblock %}
</div>
