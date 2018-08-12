#!/usr/bin/env python

import json

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ChatMessageClientPacket(BasePacket):
    PACKET_ID = 0x02
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, chat, position):
        BasePacket.__init__(self)
        self._chat = chat
        self._position = int(position)

    def get_chat(self):
        return self._chat

    def set_chat(self, chat):
        self._chat = chat

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, json.dumps(packet.get_chat()).encode("utf8"))
        StreamIO.write_byte(stream, packet.get_position())

    @staticmethod
    def read(stream, packet_size):
        chat = json.loads(StreamIO.read_string(stream).decode("utf8"))
        position = StreamIO.read_byte(stream)

        return ChatMessageClientPacket(chat, position)
