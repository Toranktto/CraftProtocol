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
        self._window_id = int(window_id)
        self._slots = slots

    def get_window_id(self):
        return self._window_id

    def set_window_id(self, window_id):
        self._window_id = int(window_id)

    def get_slots(self):
        return self._slots

    def set_slots(self, slots):
        self._slots = slots

    @staticmethod
    def write(stream, packet):
        StreamIO.write_ubyte(stream, packet.get_window_id())
        StreamIO.write_short(stream, len(packet.get_slots()))

        for slot_data in packet.get_slots():
            StreamIO.write_short(stream, slot_data.get_id())
            if slot_data.is_empty():
                StreamIO.write_byte(stream, slot_data.get_count())
                StreamIO.write_short(stream, slot_data.get_damage())
                NBTSerializer.write(stream, slot_data.get_tag())

    @staticmethod
    def read(stream, packet_size):
        window_id = StreamIO.read_ubyte(stream)
        slots_len = StreamIO.read_short(stream)
        slots = []

        for i in xrange(slots_len):
            slot_data = SlotData(StreamIO.read_short(stream))
            if not slot_data.is_empty():
                slot_data.set_count(StreamIO.read_byte(stream))
                slot_data.set_damage(StreamIO.read_short(stream))
                slot_data.set_tag(NBTSerializer.read(stream))

            slots.append(slot_data)

        return WindowItemsPacket(window_id, slots)
