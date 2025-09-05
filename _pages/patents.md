---
layout: page
permalink: /patents/
title: patents
description: Patents, https://patents.google.com/?inventor=ravi+kumar+alluboyina&litigation=NO&oq=ravi+kumar+alluboyina
nav: true
nav_order: 1
---

{% if site.data.patents.patent_list %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for patent in site.data.patents.patent_list %}
    <a class="past-title" href={{patent['link']}}>{{patent['id']}} {{patent['title']}}</a>
  {% endfor %}
</div>
