#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class HandshakePacket(BasePacket):
    PACKET_ID = 0x00
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, protocol, hostname, port, next_state):
        BasePacket.__init__(self)
        self.__protocol = int(protocol)
        self.__hostname = unicode(hostname)
        self.__port = int(port)
        self.__next_state = int(next_state)

    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol):
        self.__protocol = int(protocol)

    @property
    def hostname(self):
        return self.__hostname

    @hostname.setter
    def hostname(self, hostname):
        self.__hostname = unicode(hostname)

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.__port = int(port)

    @property
    def next_state(self):
        return self.__next_state

    @next_state.setter
    def next_state(self, next_state):
        self.__next_state = int(next_state)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_varint(stream, packet.protocol)
        StreamIO.write_string(stream, packet.hostname.encode("utf8"))
        StreamIO.write_ushort(stream, packet.port)
        StreamIO.write_varint(stream, packet.next_state)

    @staticmethod
    def read(stream, packet_size):
        protocol = StreamIO.read_varint(stream)
        hostname = StreamIO.read_string(stream).decode("utf8")
        port = StreamIO.read_ushort(stream)
        next_state = StreamIO.read_varint(stream)

        return HandshakePacket(protocol, hostname, port, next_state)
