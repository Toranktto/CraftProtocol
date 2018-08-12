#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.StreamIO import StreamIO


class NBTTagDouble(NBTBase):
    TYPE_ID = 0x06

    def __init__(self, value):
        NBTBase.__init__(self)
        self._value = float(value)

    def get(self):
        return self._value

    @staticmethod
    def write(stream, tag):
        StreamIO.write_double(stream, tag.get())

    @staticmethod
    def read(stream):
        value = StreamIO.read_double(stream)

        return NBTTagDouble(value)
