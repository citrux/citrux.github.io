---
layout: post
title:  Архив старых статей из блога
date:   2020-03-09 14:10:00 +0400
tags: math, physics, programming
---

Пока я нахожусь в поисках вдохновения, буду приводить в порядок и выкладывать сюда старые статьи своего блога в формате pdf.

{% assign pdf_files = site.static_files | where: "pdf", true %}
{% for pdf in pdf_files %}
  1. [{{ pdf.basename }}]({{ pdf.path }})
{% endfor %}
