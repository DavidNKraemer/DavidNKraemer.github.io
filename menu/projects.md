---
layout: page
title: Projects
---

## Software

<ul class="posts">
  {% for project in site.data.projects.software %}
  <li>
  <p><b><a href="{{ project.url }}">{{project.name}}</a>:</b> {{ project.description }}</p>
  </li>
  {% endfor %}
</ul>


