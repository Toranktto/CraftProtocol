#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ClientStatusPacket(BasePacket):
    PACKET_ID = 0x16
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    class Action(object):
        PERFORM_RESPAWN = 0
        REQUEST_STATS = 1
        ACHIEVEMENT = 2

    def __init__(self, action):
        BasePacket.__init__(self)
        self._action = int(action)

    def get_action(self):
        return self._action

    def set_action(self, action):
        self._action = int(action)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_varint(stream, packet.get_action())

    @staticmethod
    def read(stream, packet_size):
        action = StreamIO.read_varint(stream)

        return ClientStatusPacket(action)
