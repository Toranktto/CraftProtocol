#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ChatMessageServerPacket(BasePacket):
    PACKET_ID = 0x01
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, message):
        BasePacket.__init__(self)
        self.__message = unicode(message)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = unicode(message)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, packet.message.encode("utf8"))

    @staticmethod
    def read(stream, packet_size):
        message = StreamIO.read_string(stream).decode("utf8")

        return ChatMessageServerPacket(message)
