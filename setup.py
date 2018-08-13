#!/usr/bin/env python

from distutils.core import setup

from CraftProtocol import VersionConstants

setup(
    name="CraftProtocol",
    packages=[
        "CraftProtocol",
        "CraftProtocol.NBT",
        "CraftProtocol.Inventory",
        "CraftProtocol.Chat",
        "CraftProtocol.World",
        "CraftProtocol.Protocol",
        "CraftProtocol.Protocol.Packet",
        "CraftProtocol.Protocol.v1_8",
        "CraftProtocol.Protocol.v1_8.Packet",
        "CraftProtocol.Protocol.v1_8.Packet.Handshaking",
        "CraftProtocol.Protocol.v1_8.Packet.Status",
        "CraftProtocol.Protocol.v1_8.Packet.Login",
        "CraftProtocol.Protocol.v1_8.Packet.Play",
        "CraftProtocol.Protocol.v1_10",
        "CraftProtocol.Protocol.v1_10.Packet",
        "CraftProtocol.Protocol.v1_10.Packet.Handshaking",
        "CraftProtocol.Protocol.v1_10.Packet.Status",
        "CraftProtocol.Protocol.v1_10.Packet.Login",
        "CraftProtocol.Protocol.v1_10.Packet.Play",
        "CraftProtocol.Protocol.v1_12_2",
        "CraftProtocol.Protocol.v1_12_2.Packet",
        "CraftProtocol.Protocol.v1_12_2.Packet.Handshaking",
        "CraftProtocol.Protocol.v1_12_2.Packet.Status",
        "CraftProtocol.Protocol.v1_12_2.Packet.Login",
        "CraftProtocol.Protocol.v1_12_2.Packet.Play"
    ],
    version=VersionConstants.VERSION,
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
