#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ClientSettingsPacket(BasePacket):
    PACKET_ID = 0x15
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, locale, view_distance, chat_mode, chat_colors, skin_parts):
        BasePacket.__init__(self)
        self.__locale = unicode(locale)
        self.__view_distance = int(view_distance)
        self.__chat_mode = int(chat_mode)
        self.__chat_colors = bool(chat_colors)
        self.__skin_parts = int(skin_parts)

    @property
    def locale(self):
        return self.__locale

    @locale.setter
    def locale(self, locale):
        self.__locale = unicode(locale)

    @property
    def view_distance(self):
        return self.__view_distance

    @view_distance.setter
    def view_distance(self, view_distance):
        self.__view_distance = int(view_distance)

    @property
    def chat_mode(self):
        return self.__chat_mode

    @chat_mode.setter
    def chat_mode(self, chat_mode):
        self.__chat_mode = int(chat_mode)

    @property
    def chat_colors(self):
        return self.__chat_colors

    @chat_colors.setter
    def chat_colors(self, chat_colors):
        self.__chat_colors = bool(chat_colors)

    @property
    def skin_parts(self):
        return self.__skin_parts

    @skin_parts.setter
    def skin_parts(self, skin_parts):
        self.__skin_parts = int(skin_parts)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, packet.locale)
        StreamIO.write_byte(stream, packet.view_distance)
        StreamIO.write_varint(stream, packet.chat_mode)
        StreamIO.write_bool(stream, packet.chat_colors)
        StreamIO.write_ubyte(stream, packet.skin_parts)

    @staticmethod
    def read(stream, packet_size):
        locale = StreamIO.read_string(stream)
        view_distance = StreamIO.read_byte(stream)
        chat_mode = StreamIO.read_varint(stream)
        chat_colors = StreamIO.read_bool(stream)
        skin_parts = StreamIO.read_ubyte(stream)

        return ClientSettingsPacket(locale, view_distance, chat_mode, chat_colors, skin_parts)
