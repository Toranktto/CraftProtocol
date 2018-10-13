#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ConfirmTransactionServerPacket(BasePacket):
    PACKET_ID = 0x05
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, window_id, transaction_id, accepted):
        BasePacket.__init__(self)
        self.__window_id = int(window_id)
        self.__transaction_id = int(transaction_id)
        self.__accepted = bool(accepted)

    @property
    def window_id(self):
        return self.__window_id

    @window_id.setter
    def window_id(self, window_id):
        self.__window_id = int(window_id)

    @property
    def transaction_id(self):
        return self.__transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        self.__transaction_id = int(transaction_id)

    @property
    def accepted(self):
        return self.__accepted

    @accepted.setter
    def accepted(self, accepted):
        self.__accepted = bool(accepted)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_byte(stream, packet.window_id)
        StreamIO.write_short(stream, packet.transaction_id)
        StreamIO.write_bool(stream, packet.accepted)

    @staticmethod
    def read(stream, packet_size):
        window_id = StreamIO.read_byte(stream)
        transaction_id = StreamIO.read_short(stream)
        accepted = StreamIO.read_bool(stream)

        return ConfirmTransactionServerPacket(window_id, transaction_id, accepted)
