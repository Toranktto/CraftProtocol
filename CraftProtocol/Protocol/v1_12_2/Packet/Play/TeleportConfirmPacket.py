#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class TeleportConfirmPacket(BasePacket):
    PACKET_ID = 0x00
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, teleport_id):
        BasePacket.__init__(self)
        self.__teleport_id = int(teleport_id)

    @property
    def teleport_id(self):
        return self.__teleport_id

    @teleport_id.setter
    def teleport_id(self, teleport_id):
        self.__teleport_id = int(teleport_id)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_varint(stream, packet.teleport_id)

    @staticmethod
    def read(stream, packet_size):
        teleport_id = StreamIO.read_varint(stream)

        return TeleportConfirmPacket(teleport_id)
