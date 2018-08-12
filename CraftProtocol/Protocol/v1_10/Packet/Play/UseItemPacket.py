#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class UseItemPacket(BasePacket):
    PACKET_ID = 0x1D
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, hand_type):
        BasePacket.__init__(self)
        self._hand_type = int(hand_type)

    def get_hand_type(self):
        return self._hand_type

    def set_hand_type(self, hand_type):
        self._hand_type = int(hand_type)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_varint(stream, packet.get_hand_type())

    @staticmethod
    def read(stream, packet_size):
        hand_type = StreamIO.read_varint(stream)

        return UseItemPacket(hand_type)
