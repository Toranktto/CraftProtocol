#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.StreamIO import StreamIO


class ClientStatusPacket(BasePacket):
    PACKET_ID = 0x03
    PACKET_DIRECTION = PacketDirection.SERVERBOUND

    class Action(object):
        PERFORM_RESPAWN = 0
        REQUEST_STATS = 1
        OPEN_INVENTORY = 2

    def __init__(self, action):
        BasePacket.__init__(self)
        self.__action = int(action)

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action):
        self.__action = int(action)

    @staticmethod
    def write(stream, packet):
        StreamIO.write_varint(stream, packet.action)

    @staticmethod
    def read(stream, packet_size):
        action = StreamIO.read_varint(stream)

        return ClientStatusPacket(action)
