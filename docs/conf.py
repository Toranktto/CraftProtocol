#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

sys.path.insert(0, os.path.abspath(".."))

source_suffix = ".rst"
master_doc = "index"
project = "CraftProtocol"
year = int(time.strftime("%Y"))
copyright = u"2018%s, Łukasz Derlatka" % ("-%d" % year if year > 2018 else "")
author = "Toranktto"
version = __import__("CraftProtocol").get_version()
release = version
language = None
exclude_patterns = []
pygments_style = "sphinx"
todo_include_todos = False
html_theme = "classic"
html_static_path = ["static"]
htmlhelp_basename = "CraftProtocol_doc"
latex_elements = {}
latex_documents = [
    (master_doc, "CraftProtocol.tex", "CraftProtocol Documentation",
     "Toranktto", "manual"),
]
man_pages = [
    (master_doc, "craftprotocol", "CraftProtocol Documentation",
     [author], 1)
]
texinfo_documents = [
    (master_doc, "CraftProtocol", "CraftProtocol Documentation",
     author, "CraftProtocol", "Minecraft network protocol and NBT in Python 2.7.",
     "Miscellaneous"),
]
