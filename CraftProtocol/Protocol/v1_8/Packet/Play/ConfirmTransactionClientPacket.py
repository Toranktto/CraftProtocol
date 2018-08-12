#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ConfirmTransactionClientPacket(BasePacket):
    PACKET_ID = 0x32
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, window_id, transaction_id, accepted):
        BasePacket.__init__(self)
        self._window_id = int(window_id)
        self._transaction_id = int(transaction_id)
        self._accepted = bool(accepted)

    def get_window_id(self):
        return self._window_id

    def set_window_id(self, window_id):
        self._window_id = int(window_id)

    def get_transaction_id(self):
        return self._transaction_id

    def set_transaction_id(self, transaction_id):
        self._transaction_id = int(transaction_id)

    def is_accepted(self):
        return self._accepted

    def set_accepted(self, accepted):
        self._accepted = bool(accepted)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_byte(stream, packet.get_window_id())
        StreamIO.write_short(stream, packet.get_transaction_id())
        StreamIO.write_bool(stream, packet.is_accepted())

    @staticmethod
    def read(stream, packet_size):
        window_id = StreamIO.read_byte(stream)
        transaction_id = StreamIO.read_short(stream)
        accepted = StreamIO.read_bool(stream)

        return ConfirmTransactionClientPacket(window_id, transaction_id, accepted)
