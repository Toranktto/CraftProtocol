#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.StreamIO import StreamIO


class NBTTagShort(NBTBase):
    TYPE_ID = 0x02

    def __init__(self, value):
        NBTBase.__init__(self)
        self._value = int(value)

    def get(self):
        return self._value

    @staticmethod
    def write(stream, tag):
        StreamIO.write_short(stream, tag.get())

    @staticmethod
    def read(stream):
        value = StreamIO.read_short(stream)

        return NBTTagShort(value)
