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
        self._description = description

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, json.dumps(packet.get_description()).encode("utf8"))

    @staticmethod
    def read(stream, packet_size):
        description = json.loads(StreamIO.read_string(stream).decode("utf8"))

        return ResponsePacket(description)
