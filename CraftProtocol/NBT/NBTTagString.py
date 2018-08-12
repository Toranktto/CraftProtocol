#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.StreamIO import StreamIO


class NBTTagString(NBTBase):
    TYPE_ID = 0x08

    def __init__(self, value):
        NBTBase.__init__(self)
        self._value = unicode(value)

    def get(self):
        return self._value

    @staticmethod
    def write(stream, tag):
        StreamIO.write_ushort(stream, len(tag.get().encode("utf8")))
        StreamIO.write(stream, tag.get().encode("utf8"))

    @staticmethod
    def read(stream):
        len = StreamIO.read_ushort(stream)
        value = StreamIO.read(stream, len).decode("utf8")

        return NBTTagString(value)
