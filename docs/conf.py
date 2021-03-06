#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import time
from CraftProtocol import VersionConstants

source_suffix = ".rst"
master_doc = "index"
project = u"CraftProtocol"
copyright = u"2018-%s, Łukasz Derlatka" % (time.strftime("%Y"))
author = u"Toranktto"
version = VersionConstants.VERSION
release = VersionConstants.VERSION
language = None
exclude_patterns = []
pygments_style = "sphinx"
todo_include_todos = False
html_theme = "classic"
html_static_path = ["static"]
htmlhelp_basename = "CraftProtocoldoc"
latex_elements = {}
latex_documents = [
    (master_doc, "CraftProtocol.tex", u"CraftProtocol Documentation",
     u"Toranktto", "manual"),
]
man_pages = [
    (master_doc, "craftprotocol", u"CraftProtocol Documentation",
     [author], 1)
]
texinfo_documents = [
    (master_doc, "CraftProtocol", u"CraftProtocol Documentation",
     author, "CraftProtocol", "Minecraft network protocol and NBT in Python 2.7.",
     "Miscellaneous"),
]
