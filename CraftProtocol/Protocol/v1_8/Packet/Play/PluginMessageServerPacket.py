#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class PluginMessageServerPacket(BasePacket):
    PACKET_ID = 0x17
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, channel, plugin_bytes):
        BasePacket.__init__(self)
        self.__channel = unicode(channel)
        self.__bytes = plugin_bytes

    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, channel):
        self.__channel = unicode(channel)

    @property
    def bytes(self):
        return self.__bytes

    @bytes.setter
    def bytes(self, plugin_bytes):
        self.__bytes = plugin_bytes

    @staticmethod
    def write(stream, packet):
        StreamIO.write_string(stream, packet.channel.encode("utf8"))
        StreamIO.write(stream, packet.bytes)

    @staticmethod
    def read(stream, packet_size):
        channel_len = StreamIO.read_varint(stream)
        channel = StreamIO.read(stream, channel_len).decode("utf8")
        plugin_bytes = StreamIO.read(stream, packet_size - StreamIO.size_varint(channel_len) - channel_len)

        return PluginMessageServerPacket(channel, plugin_bytes)
