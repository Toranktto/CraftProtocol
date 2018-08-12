#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class PluginMessageServerPacket(BasePacket):
    PACKET_ID = 0x09
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, channel, plugin_bytes):
        BasePacket.__init__(self)
        self._channel = unicode(channel)
        self._bytes = plugin_bytes

    def get_channel(self):
        return self._channel

    def set_channel(self, channel):
        self._channel = unicode(channel)

    def get_bytes(self):
        return self._bytes

    def set_bytes(self, plugin_bytes):
        self._bytes = plugin_bytes

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, packet.get_channel().encode("utf8"))
        StreamIO.write(stream, packet.get_bytes())

    @staticmethod
    def read(stream, packet_size):
        channel_len = StreamIO.read_varint(stream)
        channel = StreamIO.read(stream, channel_len).decode("utf8")
        plugin_bytes = StreamIO.read(stream, packet_size - StreamIO.size_varint(channel_len) - channel_len)

        return PluginMessageServerPacket(channel, plugin_bytes)
