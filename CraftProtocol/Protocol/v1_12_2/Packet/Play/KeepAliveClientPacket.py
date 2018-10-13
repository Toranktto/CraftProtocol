#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class KeepAliveClientPacket(BasePacket):
    PACKET_ID = 0x1F
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, keepalive_id):
        BasePacket.__init__(self)
        self.__id = long(keepalive_id)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, keepalive_id):
        self.__id = long(keepalive_id)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_long(stream, packet.id)

    @staticmethod
    def read(stream, packet_size):
        keepalive_id = StreamIO.read_long(stream)

        return KeepAliveClientPacket(keepalive_id)
