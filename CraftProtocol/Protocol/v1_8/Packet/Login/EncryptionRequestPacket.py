#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class EncryptionRequestPacket(BasePacket):
    PACKET_ID = 0x01
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, server_id, public_key, verify_token):
        BasePacket.__init__(self)
        self.__server_id = unicode(server_id)
        self.__public_key = public_key
        self.__verify_token = verify_token

    @property
    def server_id(self):
        return self.__server_id

    @server_id.setter
    def server_id(self, server_id):
        self.__server_id = unicode(server_id)

    @property
    def public_key(self):
        return self.__public_key

    @public_key.setter
    def public_key(self, public_key):
        self.__public_key = public_key

    @property
    def verify_token(self):
        return self.__verify_token

    @verify_token.setter
    def verify_token(self, verify_token):
        self.__verify_token = verify_token

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, packet.server_id.encode("utf8"))
        StreamIO.write_string(stream, packet.public_key)
        StreamIO.write_string(stream, packet.verify_token)

    @staticmethod
    def read(stream, packet_size):
        server_id = StreamIO.read_string(stream).decode("utf8")
        public_key = StreamIO.read_string(stream)
        verify_token = StreamIO.read_string(stream)

        return EncryptionRequestPacket(server_id, public_key, verify_token)
