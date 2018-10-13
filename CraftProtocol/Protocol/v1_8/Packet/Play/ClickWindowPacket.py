#!/usr/bin/env python

from CraftProtocol.Inventory.SlotData import SlotData
from CraftProtocol.NBT.NBTSerializer import NBTSerializer
from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ClickWindowPacket(BasePacket):
    PACKET_ID = 0x0E
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, window_id, slot, button, transaction_id, mode, slot_data):
        BasePacket.__init__(self)
        self.__window_id = int(window_id)
        self.__slot = int(slot)
        self.__button = int(button)
        self.__transaction_id = int(transaction_id)
        self.__mode = int(mode)
        self.__slot_data = slot_data

    @property
    def window_id(self):
        return self.__window_id

    @window_id.setter
    def window_id(self, window_id):
        self.__window_id = int(window_id)

    @property
    def slot(self):
        return self.__slot

    @slot.setter
    def slot(self, slot):
        self.__slot = int(slot)

    @property
    def button(self):
        return self.__button

    @button.setter
    def button(self, button):
        self.__button = int(button)

    @property
    def transaction_id(self):
        return self.__transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        self.__transaction_id = int(transaction_id)

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode):
        self.__mode = int(mode)

    @property
    def slot_data(self):
        return self.__slot_data

    @slot_data.setter
    def slot_data(self, slot_data):
        self.__slot_data = slot_data

    @staticmethod
    def write(stream, packet):
        StreamIO.write_ubyte(stream, packet.window_id)
        StreamIO.write_short(stream, packet.slot)
        StreamIO.write_byte(stream, packet.button)
        StreamIO.write_short(stream, packet.transaction_id)
        StreamIO.write_byte(stream, packet.mode)
        StreamIO.write_short(stream, packet.slot_data.get_id())
        if not packet.slot_data.is_empty():
            StreamIO.write_byte(stream, packet.slot_data.get_count())
            StreamIO.write_short(stream, packet.slot_data.get_damage())
            NBTSerializer.write(stream, packet.slot_data.get_tag())

    @staticmethod
    def read(stream, packet_size):
        window_id = StreamIO.read_ubyte(stream)
        slot = StreamIO.read_short(stream)
        button = StreamIO.read_byte(stream)
        transaction_id = StreamIO.read_short(stream)
        mode = StreamIO.read_byte(stream)
        slot_data = SlotData(StreamIO.read_short(stream))
        if not slot_data.empty:
            slot_data.count = StreamIO.read_byte(stream)
            slot_data.damage = StreamIO.read_short(stream)
            slot_data.tag = NBTSerializer.read(stream)

        return ClickWindowPacket(window_id, slot, button, transaction_id, mode, slot_data)
