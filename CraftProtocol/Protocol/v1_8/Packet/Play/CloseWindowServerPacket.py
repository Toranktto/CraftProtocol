#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class CloseWindowServerPacket(BasePacket):
    PACKET_ID = 0x0D
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, window_id):
        BasePacket.__init__(self)
        self.__window_id = int(window_id)

    @property
    def window_id(self):
        return self.__window_id

    @window_id.setter
    def window_id(self, window_id):
        self.__window_id = int(window_id)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_ubyte(stream, packet.window_id)

    @staticmethod
    def read(stream, packet_size):
        window_id = StreamIO.read_ubyte(stream)

        return CloseWindowServerPacket(window_id)
