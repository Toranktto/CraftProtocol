#!/usr/bin/env python

from CraftProtocol.Inventory.SlotData import SlotData
from CraftProtocol.NBT.NBTSerializer import NBTSerializer
from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class PlayerBlockPlacementPacket(BasePacket):
    PACKET_ID = 0x08
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, position, face, slot_data, cursor_x, cursor_y, cursor_z):
        BasePacket.__init__(self)
        self._position = position
        self._face = int(face)
        self._slot_data = slot_data
        self._cursor_x = int(cursor_x)
        self._cursor_y = int(cursor_y)
        self._cursor_z = int(cursor_z)

    def get_position(self):
        return self._position

    def set_location(self, position):
        self._position = position

    def get_face(self):
        return self._face

    def set_face(self, face):
        self._face = int(face)

    def get_slot_data(self):
        return self._slot_data

    def set_slot_data(self, slot_data):
        self._slot_data = slot_data

    def get_cursor_x(self):
        return self._cursor_x

    def set_cursor_x(self, cursor_x):
        self._cursor_x = int(cursor_x)

    def get_cursor_y(self):
        return self._cursor_y

    def set_cursor_y(self, cursor_y):
        self._cursor_y = int(cursor_y)

    def get_cursor_z(self):
        return self._cursor_z

    def set_cursor_z(self, cursor_z):
        self._cursor_z = int(cursor_z)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_position(stream, packet.get_position())
        StreamIO.write_byte(stream, packet.get_face())
        StreamIO.write_short(stream, packet.get_slot_data().get_id())
        if packet.get_slot_data().is_empty():
            StreamIO.write_byte(stream, packet.get_slot_data().get_count())
            StreamIO.write_short(stream, packet.get_slot_data().get_damage())
            NBTSerializer.write(stream, packet.get_slot_data().get_tag())
        StreamIO.write_byte(stream, packet.get_cursor_x())
        StreamIO.write_byte(stream, packet.get_cursor_y())
        StreamIO.write_byte(stream, packet.get_cursor_z())

    @staticmethod
    def read(stream, packet_size):
        position = StreamIO.read_position(stream)
        face = StreamIO.read_byte(stream)
        slot_data = SlotData(StreamIO.read_short(stream))
        if slot_data.is_empty():
            slot_data.set_count(StreamIO.read_byte(stream))
            slot_data.set_damage(StreamIO.read_short(stream))
            slot_data.set_tag(NBTSerializer.read(stream))
        cursor_x = StreamIO.read_byte(stream)
        cursor_y = StreamIO.read_byte(stream)
        cursor_z = StreamIO.read_byte(stream)

        return PlayerBlockPlacementPacket(position, face, slot_data, cursor_x, cursor_y, cursor_z)
