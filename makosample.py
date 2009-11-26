#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pictman.py -- Picture Manager CGI"""


from mako.template import Template

param = dict(ver=0.1, title="Mako sample program")

template_str = """Content-type: text/html; charset=utf-8

<html>
  <header>
    <title>${title}</title>
  </header>
  <body>
    <h1>Mako sample program</h1>
    <p>This is Mako's sample program version ${version}.</p>
  </body>
</html>
"""

t = Template(template_str)
print t.render(param)

