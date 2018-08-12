#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class PlayerPositionAndLookClientPacket(BasePacket):
    PACKET_ID = 0x2F
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, x, y, z, yaw, pitch, flags, teleport_id):
        BasePacket.__init__(self)
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)
        self._yaw = float(yaw)
        self._pitch = float(pitch)
        self._flags = int(flags)
        self._teleport_id = int(teleport_id)

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

    def get_yaw(self):
        return self._yaw

    def set_yaw(self, yaw):
        self._yaw = float(yaw)

    def get_pitch(self):
        return self._pitch

    def set_pitch(self, pitch):
        self._pitch = float(pitch)

    def get_flags(self):
        return self._flags

    def set_flags(self, flags):
        self._flags = int(flags)

    def get_teleport_id(self):
        return self._teleport_id

    def set_teleport_id(self, teleport_id):
        self._teleport_id = int(teleport_id)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_double(stream, packet.get_x())
        StreamIO.write_double(stream, packet.get_y())
        StreamIO.write_double(stream, packet.get_z())
        StreamIO.write_float(stream, packet.get_yaw())
        StreamIO.write_float(stream, packet.get_pitch())
        StreamIO.write_byte(stream, packet.get_flags())
        StreamIO.write_varint(stream, packet.get_teleport_id())

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
