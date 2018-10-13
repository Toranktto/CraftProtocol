#!/usr/bin/env python

from CraftProtocol.Inventory.SlotData import SlotData
from CraftProtocol.NBT.NBTSerializer import NBTSerializer
from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class WindowItemsPacket(BasePacket):
    PACKET_ID = 0x30
    PACKET_DIRECTION = PacketDirection.CLIENTBOUND

    def __init__(self, window_id, slots):
        BasePacket.__init__(self)
        self.__window_id = int(window_id)
        self.__slots = slots

    @property
    def window_id(self):
        return self.__window_id

    @window_id.setter
    def window_id(self, window_id):
        self.__window_id = int(window_id)

    @property
    def slots(self):
        return self.__slots

    @slots.setter
    def slots(self, slots):
        self.__slots = slots

    @staticmethod
    def write(stream, packet):
        StreamIO.write_ubyte(stream, packet.window_id)
        StreamIO.write_short(stream, len(packet.slots))

        for slot_data in packet.slots:
            StreamIO.write_short(stream, slot_data.id)
            if not slot_data.empty:
                StreamIO.write_byte(stream, slot_data.count)
                StreamIO.write_short(stream, slot_data.damage)
                NBTSerializer.write(stream, slot_data.tag)

    @staticmethod
    def read(stream, packet_size):
        window_id = StreamIO.read_ubyte(stream)
        slots_len = StreamIO.read_short(stream)
        slots = []

        for i in xrange(slots_len):
            slot_data = SlotData(StreamIO.read_short(stream))
            if not slot_data.empty:
                slot_data.count = StreamIO.read_byte(stream)
                slot_data.damage = StreamIO.read_short(stream)
                slot_data.tag = NBTSerializer.read(stream)

            slots.append(slot_data)

        return WindowItemsPacket(window_id, slots)
