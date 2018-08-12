#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection


class RequestPacket(BasePacket):
    PACKET_ID = 0x00
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self):
        BasePacket.__init__(self)

    @staticmethod
    def write(stream, packet):
        pass  # No fields

    @staticmethod
    def read(stream, packet_size):
        return RequestPacket()
