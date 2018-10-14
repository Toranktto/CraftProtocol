#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.StreamIO import StreamIO


class NBTTagString(NBTBase):
    TYPE_ID = 0x08

    def __init__(self, value):
        NBTBase.__init__(self)
        self.__value = unicode(value)

    def get(self):
        return self.__value

    @staticmethod
    def write(stream, tag):
        StreamIO.write_ushort(stream, len(tag.get().encode("utf8")))
        StreamIO.write(stream, tag.get().encode("utf8"))

    @staticmethod
    def read(stream):
        return NBTTagString(StreamIO.read(stream, StreamIO.read_ushort(stream)).decode("utf8"))
