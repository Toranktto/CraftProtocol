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
        self._reason = reason

    def get_reason(self):
        return self._reason

    def set_reason(self, reason):
        self._reason = reason

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, json.dumps(packet.get_reason()).encode("utf8"))

    @staticmethod
    def read(stream, packet_size):
        reason = json.loads(StreamIO.read_string(stream).decode("utf8"))

        return DisconnectPacket(reason)
