#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class JoinGamePacket(BasePacket):
    PACKET_ID = 0x23
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, entity_id, gamemode, dimension, difficulty, max_players, level_type, debug_info):
        BasePacket.__init__(self)
        self.__entity_id = int(entity_id)
        self.__gamemode = int(gamemode)
        self.__dimension = int(dimension)
        self.__difficulty = int(difficulty)
        self.__max_players = int(max_players)
        self.__level_type = unicode(level_type)
        self.__debug_info = bool(debug_info)

    @property
    def entity_id(self):
        return self.__entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        self.__entity_id = int(entity_id)

    @property
    def gamemode(self):
        return self.__gamemode

    @gamemode.setter
    def gamemode(self, gamemode):
        self.__gamemode = int(gamemode)

    @property
    def dimension(self):
        return self.__dimension

    @dimension.setter
    def dimension(self, dimension):
        self.__dimension = int(dimension)

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self.__difficulty = int(difficulty)

    @property
    def max_players(self):
        return self.__max_players

    @max_players.setter
    def max_players(self, max_players):
        self.__max_players = int(max_players)

    @property
    def level_type(self):
        return self.__level_type

    @level_type.setter
    def level_type(self, level_type):
        self.__level_type = unicode(level_type)

    @property
    def debug_info(self):
        return self.__debug_info

    @debug_info.setter
    def debug_info(self, debug_info):
        self.__debug_info = bool(debug_info)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_int(stream, packet.entity_id)
        StreamIO.write_ubyte(stream, packet.gamemode)
        StreamIO.write_int(stream, packet.dimension)
        StreamIO.write_ubyte(stream, packet.difficulty)
        StreamIO.write_ubyte(stream, packet.max_players)
        StreamIO.write_string(stream, packet.level_type.encode("utf8"))
        StreamIO.write_bool(stream, packet.debug_info)

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
