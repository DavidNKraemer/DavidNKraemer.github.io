---
layout: page
title: Published papers 
---

## Journal articles

<ul class="posts">
  {% for paper in site.data.papers.journals %}
  <li>
    <p> "{{ paper.title }}" {% for author in paper.authors %} {{ author }},
    {% endfor %} ({{ paper.date }}). <i>{{ paper.publication }}</i>{% if paper.doi %}, 
    <a href="http://doi.org/{{ paper.doi }}">Link</a>{% endif %}.</p>
  </li>
  {% endfor %}
</ul>

## Proceedings papers

<ul class="posts">
  {% for paper in site.data.papers.proceedings %}
  <li>
    <p> "{{ paper.title }}" {% for author in paper.authors %} {{ author }},
    {% endfor %} ({{ paper.date }}). <i>{{ paper.publication }}</i>{% if paper.doi %}, 
    <a href="http://doi.org/{{ paper.doi }}">Link</a>{% endif %}.</p>
  </li>
  {% endfor %}
</ul>

