#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.StreamIO import StreamIO


class NBTTagLong(NBTBase):
    TYPE_ID = 0x04

    def __init__(self, value):
        NBTBase.__init__(self)
        self.__value = long(value)

    def get(self):
        return self.__value

    @staticmethod
    def write(stream, tag):
        StreamIO.write_long(stream, tag.get())

    @staticmethod
    def read(stream):
        return NBTTagLong(StreamIO.read_long(stream))
