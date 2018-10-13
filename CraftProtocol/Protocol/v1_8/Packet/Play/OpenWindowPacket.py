#!/usr/bin/env python

import json

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class OpenWindowPacket(BasePacket):
    PACKET_ID = 0x2D
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, window_id, window_type, window_title, slots_number, entity_id=None):
        BasePacket.__init__(self)
        self.__window_id = int(window_id)
        self.__window_type = unicode(window_type)
        self.__window_title = window_title
        self.__slots_number = int(slots_number)

        if entity_id is not None:
            entity_id = int(entity_id)

        self.__entity_id = entity_id

    @property
    def window_id(self):
        return self.__window_id

    @window_id.setter
    def window_id(self, window_id):
        self.__window_id = int(window_id)

    @property
    def window_type(self):
        return self.__window_type

    @window_type.setter
    def window_type(self, window_type):
        self.__window_type = unicode(window_type)

    @property
    def window_title(self):
        return self.__window_title

    @window_title.setter
    def window_title(self, window_title):
        self.__window_title = window_title

    @property
    def slots_number(self):
        return self.__slots_number

    @slots_number.setter
    def slots_number(self, slots_number):
        self.__slots_number = int(slots_number)

    @property
    def entity_id(self):
        return self.__entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        if entity_id is not None:
            entity_id = int(entity_id)

        self.__entity_id = entity_id

    @staticmethod
    def write(stream, packet):
        StreamIO.write_ubyte(stream, packet.window_id)
        StreamIO.write_string(stream, packet.window_type.encode("utf8"))
        StreamIO.write_string(stream, json.dumps(packet.window_title).encode("utf8"))
        StreamIO.write_ubyte(stream, packet.slots_number)
        if packet.window_type == "EntityHorse":
            StreamIO.write_int(stream, packet.entity_id)

    @staticmethod
    def read(stream, packet_size):
        window_id = StreamIO.read_ubyte(stream)
        window_type = StreamIO.read_string(stream).decode("utf8")
        window_title = json.loads(StreamIO.read_string(stream).decode("utf8"))
        slots_number = StreamIO.read_ubyte(stream)
        entity_id = None
        if window_type == "EntityHorse":
            entity_id = StreamIO.read_int(stream)

        return OpenWindowPacket(window_id, window_type, window_title, slots_number, entity_id)
