#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.StreamIO import StreamIO


class NBTTagLong(NBTBase):
    TYPE_ID = 0x04

    def __init__(self, value):
        NBTBase.__init__(self)
        self._value = long(value)

    def get(self):
        return self._value

    @staticmethod
    def write(stream, tag):
        StreamIO.write_long(stream, tag.get())

    @staticmethod
    def read(stream):
        value = StreamIO.read_long(stream)

        return NBTTagLong(value)
