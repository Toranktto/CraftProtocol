#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class PlayerPositionAndLookClientPacket(BasePacket):
    PACKET_ID = 0x2F
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, x, y, z, yaw, pitch, flags, teleport_id):
        BasePacket.__init__(self)
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)
        self.__yaw = float(yaw)
        self.__pitch = float(pitch)
        self.__flags = int(flags)
        self.__teleport_id = int(teleport_id)

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
    def yaw(self):
        return self.__yaw

    @yaw.setter
    def yaw(self, yaw):
        self.__yaw = float(yaw)

    @property
    def pitch(self):
        return self.__pitch

    @pitch.setter
    def pitch(self, pitch):
        self.__pitch = float(pitch)

    @property
    def flags(self):
        return self.__flags

    @flags.setter
    def flags(self, flags):
        self.__flags = int(flags)

    @property
    def teleport_id(self):
        return self.__teleport_id

    @teleport_id.setter
    def teleport_id(self, teleport_id):
        self.__teleport_id = int(teleport_id)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_double(stream, packet.x)
        StreamIO.write_double(stream, packet.y)
        StreamIO.write_double(stream, packet.z)
        StreamIO.write_float(stream, packet.yaw)
        StreamIO.write_float(stream, packet.pitch)
        StreamIO.write_byte(stream, packet.flags)
        StreamIO.write_varint(stream, packet.teleport_id)

    @staticmethod
    def read(stream, packet_size):
        x = StreamIO.read_double(stream)
        y = StreamIO.read_double(stream)
        z = StreamIO.read_double(stream)
        yaw = StreamIO.read_float(stream)
        pitch = StreamIO.read_float(stream)
        flags = StreamIO.read_byte(stream)
        teleport_id = StreamIO.read_varint(stream)

        return PlayerPositionAndLookClientPacket(x, y, z, yaw, pitch, flags, teleport_id)
