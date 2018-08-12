#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class HeldItemChangeServerPacket(BasePacket):
    PACKET_ID = 0x09
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, slot):
        BasePacket.__init__(self)
        self._slot = int(slot)

    def get_slot(self):
        return self._slot

    def set_slot(self, slot):
        self._slot = int(slot)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_short(stream, packet.get_slot())

    @staticmethod
    def read(stream, packet_size):
        slot = StreamIO.read_short(stream)

        return HeldItemChangeServerPacket(slot)
