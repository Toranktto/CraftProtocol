#!/usr/bin/env python

from setuptools import setup, find_packages


def read(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()

    return data


setup(
    name="CraftProtocol",
    packages=find_packages(exclude=["tests"]),
    version=__import__("CraftProtocol").get_version(),
    description="Minecraft network protocol and NBT in Python 2.7.",
    long_description=read("README.md"),
    author="Toranktto",
    test_suite="tests",
    url="https://github.com/Toranktto/CraftProtocol",
    license="MIT",
    author_email="toranktto@gmail.com",
    extras_require={
        "lint_test": "pylint"
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License"
    ]
)
