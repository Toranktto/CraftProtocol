#!/usr/bin/env python

import json

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ResponsePacket(BasePacket):
    PACKET_ID = 0x00
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, description):
        BasePacket.__init__(self)
        self.__description = description

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, json.dumps(packet.description).encode("utf8"))

    @staticmethod
    def read(stream, packet_size):
        description = json.loads(StreamIO.read_string(stream).decode("utf8"))

        return ResponsePacket(description)
