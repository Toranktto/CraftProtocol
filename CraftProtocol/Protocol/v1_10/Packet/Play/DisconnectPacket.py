#!/usr/bin/env python

import json

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class DisconnectPacket(BasePacket):
    PACKET_ID = 0x1A
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, reason):
        BasePacket.__init__(self)
        self.__reason = reason

    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, reason):
        self.__reason = reason

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, json.dumps(packet.reason).encode("utf8"))

    @staticmethod
    def read(stream, packet_size):
        reason = json.loads(StreamIO.read_string(stream).decode("utf8"))

        return DisconnectPacket(reason)
