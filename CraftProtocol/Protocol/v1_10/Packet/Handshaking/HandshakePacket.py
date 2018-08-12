#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class HandshakePacket(BasePacket):
    PACKET_ID = 0x00
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    def __init__(self, protocol, hostname, port, next_state):
        BasePacket.__init__(self)
        self._protocol = int(protocol)
        self._hostname = unicode(hostname)
        self._port = int(port)
        self._next_state = int(next_state)

    def get_protocol(self):
        return self._protocol

    def set_protocol(self, protocol):
        self._protocol = int(protocol)

    def get_hostname(self):
        return self._hostname

    def set_hostname(self, hostname):
        self._hostname = unicode(hostname)

    def get_port(self):
        return self._port

    def set_port(self, port):
        self._port = int(port)

    def get_next_state(self):
        return self._next_state

    def set_next_state(self, next_state):
        self._next_state = int(next_state)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_varint(stream, packet.get_protocol())
        StreamIO.write_string(stream, packet.get_hostname().encode("utf8"))
        StreamIO.write_ushort(stream, packet.get_port())
        StreamIO.write_varint(stream, packet.get_next_state())

    @staticmethod
    def read(stream, packet_size):
        protocol = StreamIO.read_varint(stream)
        hostname = StreamIO.read_string(stream).decode("utf8")
        port = StreamIO.read_ushort(stream)
        next_state = StreamIO.read_varint(stream)

        return HandshakePacket(protocol, hostname, port, next_state)
