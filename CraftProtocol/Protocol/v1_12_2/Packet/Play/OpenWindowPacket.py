#!/usr/bin/env python

import json

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class OpenWindowPacket(BasePacket):
    PACKET_ID = 0x13
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, window_id, window_type, window_title, slots_number, entity_id=None):
        BasePacket.__init__(self)
        self._window_id = int(window_id)
        self._window_type = unicode(window_type)
        self._window_title = window_title
        self._slots_number = int(slots_number)

        if entity_id is not None:
            entity_id = int(entity_id)

        self._entity_id = entity_id

    def get_window_id(self):
        return self._window_id

    def set_window_id(self, window_id):
        self._window_id = int(window_id)

    def get_window_type(self):
        return self._window_type

    def set_window_type(self, window_type):
        self._window_type = unicode(window_type)

    def get_window_title(self):
        return self._window_title

    def set_window_title(self, window_title):
        self._window_title = window_title

    def get_slots_number(self):
        return self._slots_number

    def set_slots_number(self, slots_number):
        self._slots_number = int(slots_number)

    def get_entity_id(self):
        return self._entity_id

    def set_entity_id(self, entity_id):
        if entity_id is not None:
            entity_id = int(entity_id)

        self._entity_id = entity_id

    @staticmethod
    def write(stream, packet):
        StreamIO.write_ubyte(stream, packet.get_window_id())
        StreamIO.write_string(stream, packet.get_window_type().encode("utf8"))
        StreamIO.write_string(stream, json.dumps(packet.get_window_title()).encode("utf8"))
        StreamIO.write_ubyte(stream, packet.get_slots_number())
        if packet.get_window_type() == "EntityHorse":
            StreamIO.write_int(stream, packet.get_entity_id())

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
