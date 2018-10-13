#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class PlayerPositionServerPacket(BasePacket):
    PACKET_ID = 0x04
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, x, y, z, on_ground):
        BasePacket.__init__(self)
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)
        self.__on_ground = bool(on_ground)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = float(x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = float(y)

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z):
        self.__z = float(z)

    @property
    def on_ground(self):
        return self.__on_ground

    @on_ground.setter
    def on_ground(self, on_ground):
        self.__on_ground = bool(on_ground)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_double(stream, packet.x)
        StreamIO.write_double(stream, packet.y)
        StreamIO.write_double(stream, packet.z)
        StreamIO.write_bool(stream, packet.on_ground)

    @staticmethod
    def read(stream, packet_size):
        x = StreamIO.read_double(stream)
        y = StreamIO.read_double(stream)
        z = StreamIO.read_double(stream)
        on_ground = StreamIO.read_bool(stream)

        return PlayerPositionServerPacket(x, y, z, on_ground)
