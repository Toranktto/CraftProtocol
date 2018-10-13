#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class UseItemPacket(BasePacket):
    PACKET_ID = 0x1D
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, hand_type):
        BasePacket.__init__(self)
        self.__hand_type = int(hand_type)

    @property
    def hand_type(self):
        return self.__hand_type

    @hand_type.setter
    def hand_type(self, hand_type):
        self.__hand_type = int(hand_type)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_varint(stream, packet.hand_type)

    @staticmethod
    def read(stream, packet_size):
        hand_type = StreamIO.read_varint(stream)

        return UseItemPacket(hand_type)
