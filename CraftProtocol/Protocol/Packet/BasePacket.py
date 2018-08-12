#!/usr/bin/env python


class BasePacket(object):
    PACKET_ID = None
    PACKET_DIRECTION = None

    def __init__(self):
        pass

    @staticmethod
    def write(stream, packet):
        raise NotImplementedError()

    @staticmethod
    def read(stream, packet_size):
        raise NotImplementedError()
