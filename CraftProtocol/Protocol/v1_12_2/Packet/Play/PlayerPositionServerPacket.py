#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class PlayerPositionServerPacket(BasePacket):
    PACKET_ID = 0x0D
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, x, y, z, on_ground):
        BasePacket.__init__(self)
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)
        self._on_ground = bool(on_ground)

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = float(x)

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = float(y)

    def get_z(self):
        return self._z

    def set_z(self, z):
        self._z = float(z)

    def is_on_ground(self):
        return self._on_ground

    def set_on_ground(self, on_ground):
        self._on_ground = bool(on_ground)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_double(stream, packet.get_x())
        StreamIO.write_double(stream, packet.get_y())
        StreamIO.write_double(stream, packet.get_z())
        StreamIO.write_bool(stream, packet.is_on_ground())

    @staticmethod
    def read(stream, packet_size):
        x = StreamIO.read_double(stream)
        y = StreamIO.read_double(stream)
        z = StreamIO.read_double(stream)
        on_ground = StreamIO.read_bool(stream)

        return PlayerPositionServerPacket(x, y, z, on_ground)
