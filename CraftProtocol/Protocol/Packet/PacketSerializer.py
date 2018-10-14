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
        self.__protocol = int(protocol)
        self.__mode = int(mode)
        self.__state = ProtocolState.HANDSHAKING
        self.__threshold = -1

    def is_compression_enabled(self):
        return self.threshold >= 0

    @property
    def threshold(self):
        return self.__threshold

    @threshold.setter
    def threshold(self, value):
        self.__threshold = int(value)

    @property
    def protocol(self):
        return self.__protocol

    @property
    def mode(self):
        return self.__mode

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = int(state)

    def write(self, stream, packet):
        assert packet.__class__.PACKET_DIRECTION == PacketDirection.SERVERBOUND \
            if self.__mode == PacketSerializer.Mode.CLIENT else \
            packet.__class__.PACKET_DIRECTION == PacketDirection.CLIENTBOUND, \
            "packet has invalid direction for this serializer"

        buf = StringIO()
        StreamIO.write_varint(buf, packet.__class__.PACKET_ID)
        packet.__class__.write(buf, packet)
        data = buf.getvalue()
        buf.close()

        if self.is_compression_enabled():
            buf = StringIO()

            if len(data) >= self.threshold:
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
                packet_size -= StreamIO.size_varint(data_size)
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

        packet_direction = None
        if self.__mode == PacketSerializer.Mode.SERVER:
            packet_direction = PacketDirection.SERVERBOUND
        elif self.__mode == PacketSerializer.Mode.CLIENT:
            packet_direction = PacketDirection.CLIENTBOUND

        try:
            packet_class = PacketProvider.get_packet_class(self.protocol, self.state, packet_direction, packet_id)
        except KeyError:
            packet_class = BasePacket.__class__

        packet = packet_class.read(buf, packet_size)
        buf.close()

        return packet
