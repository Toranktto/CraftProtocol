#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ClientSettingsPacket(BasePacket):
    PACKET_ID = 0x15
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, locale, view_distance, chat_mode, chat_colors, skin_parts):
        BasePacket.__init__(self)
        self._locale = unicode(locale)
        self._view_distance = int(view_distance)
        self._chat_mode = int(chat_mode)
        self._chat_colors = bool(chat_colors)
        self._skin_parts = int(skin_parts)

    def get_locale(self):
        return self._locale

    def set_locale(self, locale):
        self._locale = unicode(locale)

    def get_view_distance(self):
        return self._view_distance

    def set_view_distance(self, view_distance):
        self._view_distance = int(view_distance)

    def get_chat_mode(self):
        return self._chat_mode

    def set_chat_mode(self, chat_mode):
        self._chat_mode = int(chat_mode)

    def is_chat_colors(self):
        return self._chat_colors

    def set_chat_colors(self, chat_colors):
        self._chat_colors = bool(chat_colors)

    def get_skin_parts(self):
        return self._skin_parts

    def set_skin_parts(self, skin_parts):
        self._skin_parts = int(skin_parts)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, packet.get_locale())
        StreamIO.write_byte(stream, packet.get_view_distance())
        StreamIO.write_varint(stream, packet.get_chat_mode())
        StreamIO.write_bool(stream, packet.is_chat_colors())
        StreamIO.write_ubyte(stream, packet.get_skin_parts())

    @staticmethod
    def read(stream, packet_size):
        locale = StreamIO.read_string(stream)
        view_distance = StreamIO.read_byte(stream)
        chat_mode = StreamIO.read_varint(stream)
        chat_colors = StreamIO.read_bool(stream)
        skin_parts = StreamIO.read_ubyte(stream)

        return ClientSettingsPacket(locale, view_distance, chat_mode, chat_colors, skin_parts)
