#!/usr/bin/env python

from CraftProtocol.Inventory.SlotData import SlotData
from CraftProtocol.NBT.NBTSerializer import NBTSerializer
from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ClickWindowPacket(BasePacket):
    PACKET_ID = 0x07
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, window_id, slot, button, transaction_id, mode, slot_data):
        BasePacket.__init__(self)
        self._window_id = int(window_id)
        self._slot = int(slot)
        self._button = int(button)
        self._transaction_id = int(transaction_id)
        self._mode = int(mode)
        self._slot_data = slot_data

    def get_window_id(self):
        return self._window_id

    def set_window_id(self, window_id):
        self._window_id = int(window_id)

    def get_slot(self):
        return self._slot

    def set_slot(self, slot):
        self._slot = int(slot)

    def get_button(self):
        return self._button

    def set_button(self, button):
        self._button = int(button)

    def get_transaction_id(self):
        return self._transaction_id

    def set_transaction_id(self, transaction_id):
        self._transaction_id = int(transaction_id)

    def get_mode(self):
        return self._mode

    def set_mode(self, mode):
        self._mode = int(mode)

    def get_slot_data(self):
        return self._slot_data

    def set_slot_data(self, slot_data):
        self._slot_data = slot_data

    @staticmethod
    def write(stream, packet):
        StreamIO.write_ubyte(stream, packet.get_window_id())
        StreamIO.write_short(stream, packet.get_slot())
        StreamIO.write_byte(stream, packet.get_button())
        StreamIO.write_short(stream, packet.get_transaction_id())
        StreamIO.write_varint(stream, packet.get_mode())
        StreamIO.write_short(stream, packet.get_slot_data().get_id())
        if packet.get_itemstack().get_id() != -1:
            StreamIO.write_byte(stream, packet.get_slot_data().get_count())
            StreamIO.write_short(stream, packet.get_slot_data().get_damage())
            NBTSerializer.write(stream, packet.get_slot_data().get_tag())

    @staticmethod
    def read(stream, packet_size):
        window_id = StreamIO.read_ubyte(stream)
        slot = StreamIO.read_short(stream)
        button = StreamIO.read_byte(stream)
        transaction_id = StreamIO.read_short(stream)
        mode = StreamIO.read_varint(stream)
        slot_data = SlotData(StreamIO.read_short(stream))
        if slot_data.get_id() != -1:
            slot_data.set_count(StreamIO.read_byte(stream))
            slot_data.set_damage(StreamIO.read_short(stream))
            slot_data.set_tag(NBTSerializer.read(stream))

        return ClickWindowPacket(window_id, slot, button, transaction_id, mode, slot_data)
