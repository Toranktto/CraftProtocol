#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class CloseWindowServerPacket(BasePacket):
    PACKET_ID = 0x08
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, window_id):
        BasePacket.__init__(self)
        self._window_id = int(window_id)

    def get_window_id(self):
        return self._window_id

    def set_window_id(self, window_id):
        self._window_id = int(window_id)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_ubyte(stream, packet.get_window_id())

    @staticmethod
    def read(stream, packet_size):
        window_id = StreamIO.read_ubyte(stream)

        return CloseWindowServerPacket(window_id)
