#!/usr/bin/env python

from distutils.core import setup
from pkgutil import walk_packages

import CraftProtocol


def find_packages(path, prefix):
    packages = [prefix]

    prefix = prefix + "."
    for _, name, is_pkg in walk_packages(path, prefix):
        if is_pkg:
            packages.append(name)

    return packages


setup(
    name="CraftProtocol",
    packages=find_packages(CraftProtocol.__path__, CraftProtocol.__name__),
    version=CraftProtocol.VersionConstants.VERSION,
    description="Minecraft network protocol and NBT in Python 2.7.",
    author="Toranktto",
    url="https://github.com/Toranktto/CraftProtocol",
    license="MIT",
    author_email="toranktto@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License"
    ]
)
