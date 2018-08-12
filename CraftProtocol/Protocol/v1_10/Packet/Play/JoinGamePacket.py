#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class JoinGamePacket(BasePacket):
    PACKET_ID = 0x23
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, entity_id, gamemode, dimension, difficulty, max_players, level_type, debug_info):
        BasePacket.__init__(self)
        self._entity_id = int(entity_id)
        self._gamemode = int(gamemode)
        self._dimension = int(dimension)
        self._difficulty = int(difficulty)
        self._max_players = int(max_players)
        self._level_type = unicode(level_type)
        self._debug_info = bool(debug_info)

    def get_entity_id(self):
        return self._entity_id

    def set_entity_id(self, entity_id):
        self._entity_id = int(entity_id)

    def get_gamemode(self):
        return self._gamemode

    def set_gamemode(self, gamemode):
        self._gamemode = int(gamemode)

    def get_dimension(self):
        return self._dimension

    def set_dimension(self, dimension):
        self._dimension = int(dimension)

    def get_difficulty(self):
        return self._difficulty

    def set_difficulty(self, difficulty):
        self._difficulty = int(difficulty)

    def get_max_players(self):
        return self._max_players

    def set_max_players(self, max_players):
        self._max_players = int(max_players)

    def get_level_type(self):
        return self._level_type

    def set_level_type(self, level_type):
        self._level_type = unicode(level_type)

    def is_debug_info(self):
        return self._debug_info

    def set_debug_info(self, debug_info):
        self._debug_info = bool(debug_info)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_int(stream, packet.get_entity_id())
        StreamIO.write_ubyte(stream, packet.get_gamemode())
        StreamIO.write_int(stream, packet.get_dimension())
        StreamIO.write_ubyte(stream, packet.get_difficulty())
        StreamIO.write_ubyte(stream, packet.get_max_players())
        StreamIO.write_string(stream, packet.get_level_type().encode("utf8"))
        StreamIO.write_bool(stream, packet.is_debug_info())

    @staticmethod
    def read(stream, packet_size):
        entity_id = StreamIO.read_int(stream)
        gamemode = StreamIO.read_ubyte(stream)
        dimension = StreamIO.read_int(stream)
        difficulty = StreamIO.read_ubyte(stream)
        max_players = StreamIO.read_ubyte(stream)
        level_type = StreamIO.read_string(stream).decode("utf8")
        debug_info = StreamIO.read_bool(stream)

        return JoinGamePacket(entity_id, gamemode, dimension, difficulty, max_players, level_type, debug_info)
