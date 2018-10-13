#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class LoginStartPacket(BasePacket):
    PACKET_ID = 0x00
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, username):
        BasePacket.__init__(self)
        self.__username = unicode(username)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = unicode(username)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, packet.username.encode("utf8"))

    @staticmethod
    def read(stream, packet_size):
        username = StreamIO.read_string(stream).decode("utf8")

        return LoginStartPacket(username)
