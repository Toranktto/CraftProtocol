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
        self.__position = position
        self.__face = int(face)
        self.__slot_data = slot_data
        self.__cursor_x = int(cursor_x)
        self.__cursor_y = int(cursor_y)
        self.__cursor_z = int(cursor_z)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def face(self):
        return self.__face

    @face.setter
    def face(self, face):
        self.__face = int(face)

    @property
    def slot_data(self):
        return self.__slot_data

    @slot_data.setter
    def slot_data(self, slot_data):
        self.__slot_data = slot_data

    @property
    def cursor_x(self):
        return self.__cursor_x

    @cursor_x.setter
    def cursor_x(self, cursor_x):
        self.__cursor_x = int(cursor_x)

    @property
    def cursor_y(self):
        return self.__cursor_y

    @cursor_y.setter
    def cursor_y(self, cursor_y):
        self.__cursor_y = int(cursor_y)

    @property
    def cursor_z(self):
        return self.__cursor_z

    @cursor_z.setter
    def cursor_z(self, cursor_z):
        self.__cursor_z = int(cursor_z)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_position(stream, packet.position)
        StreamIO.write_byte(stream, packet.face)
        StreamIO.write_short(stream, packet.slot_data.get_id())
        if not packet.slot_data.is_empty():
            StreamIO.write_byte(stream, packet.slot_data.get_count())
            StreamIO.write_short(stream, packet.slot_data.get_damage())
            NBTSerializer.write(stream, packet.slot_data.get_tag())
        StreamIO.write_byte(stream, packet.cursor_x)
        StreamIO.write_byte(stream, packet.cursor_y)
        StreamIO.write_byte(stream, packet.cursor_z)

    @staticmethod
    def read(stream, packet_size):
        position = StreamIO.read_position(stream)
        face = StreamIO.read_byte(stream)
        slot_data = SlotData(StreamIO.read_short(stream))
        if not slot_data.empty:
            slot_data.count = StreamIO.read_byte(stream)
            slot_data.damage = StreamIO.read_short(stream)
            slot_data.tag = NBTSerializer.read(stream)
        cursor_x = StreamIO.read_byte(stream)
        cursor_y = StreamIO.read_byte(stream)
        cursor_z = StreamIO.read_byte(stream)

        return PlayerBlockPlacementPacket(position, face, slot_data, cursor_x, cursor_y, cursor_z)
