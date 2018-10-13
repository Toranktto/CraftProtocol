#!/usr/bin/env python

import json

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ChatMessageClientPacket(BasePacket):
    PACKET_ID = 0x0F
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, chat, position):
        BasePacket.__init__(self)
        self.__chat = chat
        self.__position = int(position)

    @property
    def chat(self):
        return self.__chat

    @chat.setter
    def chat(self, chat):
        self.__chat = chat

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, json.dumps(packet.chat).encode("utf8"))
        StreamIO.write_byte(stream, packet.position)

    @staticmethod
    def read(stream, packet_size):
        chat = json.loads(StreamIO.read_string(stream).decode("utf8"))
        position = StreamIO.read_byte(stream)

        return ChatMessageClientPacket(chat, position)
