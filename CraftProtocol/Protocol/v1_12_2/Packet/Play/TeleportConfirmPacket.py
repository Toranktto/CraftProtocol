#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class TeleportConfirmPacket(BasePacket):
    PACKET_ID = 0x00
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, teleport_id):
        BasePacket.__init__(self)
        self._teleport_id = int(teleport_id)

    def get_teleport_id(self):
        return self._teleport_id

    def set_teleport_id(self, teleport_id):
        self._teleport_id = int(teleport_id)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_varint(stream, packet.get_teleport_id())

    @staticmethod
    def read(stream, packet_size):
        teleport_id = StreamIO.read_varint(stream)

        return TeleportConfirmPacket(teleport_id)
