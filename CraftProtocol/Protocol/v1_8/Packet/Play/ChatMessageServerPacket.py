#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ChatMessageServerPacket(BasePacket):
    PACKET_ID = 0x01
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, message):
        BasePacket.__init__(self)
        self._message = unicode(message)

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = unicode(message)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, packet.get_message().encode("utf8"))

    @staticmethod
    def read(stream, packet_size):
        message = StreamIO.read_string(stream).decode("utf8")

        return ChatMessageServerPacket(message)
