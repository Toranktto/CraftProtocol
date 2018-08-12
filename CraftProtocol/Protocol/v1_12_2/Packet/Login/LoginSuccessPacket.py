#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class LoginSuccessPacket(BasePacket):
    PACKET_ID = 0x02
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, uuid, username):
        BasePacket.__init__(self)
        self._uuid = unicode(uuid)
        self._username = unicode(username)

    def get_uuid(self):
        return self._uuid

    def set_uuid(self, uuid):
        self._uuid = unicode(uuid)

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = unicode(username)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, packet.get_uuid().encode("utf8"))
        StreamIO.write_string(stream, packet.get_username().encode("utf8"))

    @staticmethod
    def read(stream, packet_size):
        uuid = StreamIO.read_string(stream).decode("utf8")
        username = StreamIO.read_string(stream).decode("utf8")

        return LoginSuccessPacket(uuid, username)
