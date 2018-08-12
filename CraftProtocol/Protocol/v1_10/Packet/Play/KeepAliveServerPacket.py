#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class KeepAliveServerPacket(BasePacket):
    PACKET_ID = 0x0B
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, keepalive_id):
        BasePacket.__init__(self)
        self._id = int(keepalive_id)

    def get_id(self):
        return self._id

    def set_id(self, keepalive_id):
        self._id = int(keepalive_id)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_varint(stream, packet.get_id())

    @staticmethod
    def read(stream, packet_size):
        keepalive_id = StreamIO.read_varint(stream)

        return KeepAliveServerPacket(keepalive_id)
