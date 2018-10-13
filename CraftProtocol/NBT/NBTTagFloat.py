#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.StreamIO import StreamIO


class NBTTagFloat(NBTBase):
    TYPE_ID = 0x05

    def __init__(self, value):
        NBTBase.__init__(self)
        self.__value = float(value)

    def get(self):
        return self.__value

    @staticmethod
    def write(stream, tag):
        StreamIO.write_float(stream, tag.get())

    @staticmethod
    def read(stream):
        value = StreamIO.read_float(stream)

        return NBTTagFloat(value)
