#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class LoginSuccessPacket(BasePacket):
    PACKET_ID = 0x02
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, uuid, username):
        BasePacket.__init__(self)
        self.__uuid = unicode(uuid)
        self.__username = unicode(username)

    @property
    def uuid(self):
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid):
        self.__uuid = unicode(uuid)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = unicode(username)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, packet.uuid.encode("utf8"))
        StreamIO.write_string(stream, packet.username.encode("utf8"))

    @staticmethod
    def read(stream, packet_size):
        uuid = StreamIO.read_string(stream).decode("utf8")
        username = StreamIO.read_string(stream).decode("utf8")

        return LoginSuccessPacket(uuid, username)
