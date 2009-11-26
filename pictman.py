#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pictman.py -- Picture Manager CGI"""

from bigblack.bigblack import BigBlack
import os.path
#from  bigblack.tinycfg import TinyCfg

from mako.template import Template

class MyCGI(BigBlack):
    version = 0.1
    template_dir = "./template"
    cache_dir = "./cache"

    def __init__(self):
        BigBlack.__init__(self)

    def root(self):
#        print self.get_config("storage_dir")
        fname = os.path.join(self.template_dir, "root.html")
        t = Template(filename=fname, module_directory=self.cache_dir)
        print t.render(version=self.version, title="test")
        


bb = MyCGI()
bb.run()



