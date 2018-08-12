#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class HeldItemChangeClientPacket(BasePacket):
    PACKET_ID = 0x3A
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, slot):
        BasePacket.__init__(self)
        self._slot = int(slot)

    def get_slot(self):
        return self._slot

    def set_slot(self, slot):
        self._slot = int(slot)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_byte(stream, packet.get_slot())

    @staticmethod
    def read(stream, packet_size):
        slot = StreamIO.read_byte(stream)

        return HeldItemChangeClientPacket(slot)
