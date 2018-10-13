#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="CraftProtocol",
    packages=find_packages(exclude=["tests"]),
    version=__import__("CraftProtocol").get_version(),
    description="Minecraft network protocol and NBT in Python 2.7.",
    long_description=open("README.md").read(),
    author="Toranktto",
    test_suite="tests",
    url="https://github.com/Toranktto/CraftProtocol",
    license="MIT",
    author_email="toranktto@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License"
    ]
)
