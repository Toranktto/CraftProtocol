#!/usr/bin/env python

import zlib
from cStringIO import StringIO

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.Protocol.Packet.PacketProvider import PacketProvider
from CraftProtocol.Protocol.ProtocolState import ProtocolState
from CraftProtocol.StreamIO import StreamIO


class PacketSerializer(object):
    class Mode(object):
        CLIENT = 0
        SERVER = 1

    def __init__(self, protocol, mode):
        self._protocol = int(protocol)
        self._mode = int(mode)
        self._state = ProtocolState.HANDSHAKING
        self._threshold = -1

    def set_threshold(self, value):
        self._threshold = int(value)

    def is_compression_enabled(self):
        return self._threshold >= 0

    def get_threshold(self):
        return self._threshold

    def get_protocol(self):
        return self._protocol

    def get_mode(self):
        return self._mode

    def set_state(self, state):
        self._state = int(state)

    def get_state(self):
        return self._state

    def write(self, stream, packet):
        assert packet.__class__.PACKET_DIRECTION == PacketDirection.SERVERBOUND \
            if self._mode == PacketSerializer.Mode.CLIENT else \
            packet.__class__.PACKET_DIRECTION == PacketDirection.CLIENTBOUND, \
            "packet has invalid direction for this serializer"

        buf = StringIO()
        StreamIO.write_varint(buf, packet.__class__.PACKET_ID)
        packet.__class__.write(buf, packet)
        data = buf.getvalue()
        buf.close()

        if self.is_compression_enabled():
            buf = StringIO()

            if len(data) >= self.get_threshold():
                StreamIO.write_varint(buf, len(data))
                data = zlib.compress(data)
            else:
                StreamIO.write_varint(buf, 0)

            StreamIO.write(buf, data)
            data = buf.getvalue()
            buf.close()

        buf = StringIO()
        StreamIO.write_string(buf, data)
        data = buf.getvalue()
        buf.close()

        StreamIO.write(stream, data)

    def read(self, stream):
        packet_size = StreamIO.read_varint(stream)

        if self.is_compression_enabled():
            data_size = StreamIO.read_varint(stream)

            if data_size == 0:
                packet_size -= StreamIO.size_varint(0)
                data = StreamIO.read(stream, packet_size)
            else:
                data = StreamIO.read(stream, packet_size - StreamIO.size_varint(data_size))
                data = zlib.decompress(data)
                packet_size = data_size
        else:
            data = StreamIO.read(stream, packet_size)

        buf = StringIO(data)
        packet_id = StreamIO.read_varint(buf)
        packet_size -= StreamIO.size_varint(packet_id)

        if self._mode == PacketSerializer.Mode.SERVER:
            packet_direction = PacketDirection.SERVERBOUND
        elif self._mode == PacketSerializer.Mode.CLIENT:
            packet_direction = PacketDirection.CLIENTBOUND

        try:
            packet_class = PacketProvider.get_packet_class(self._protocol, self._state, packet_direction, packet_id)
        except KeyError:
            buf.close()
            return BasePacket()  # Unknown packet

        packet = packet_class.read(buf, packet_size)
        buf.close()

        return packet
