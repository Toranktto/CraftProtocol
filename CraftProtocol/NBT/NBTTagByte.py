#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.StreamIO import StreamIO


class NBTTagByte(NBTBase):
    TYPE_ID = 0x01

    def __init__(self, value):
        NBTBase.__init__(self)
        self.__value = int(value)

    def get(self):
        return self.__value

    @staticmethod
    def write(stream, tag):
        StreamIO.write_byte(tag.get())

    @staticmethod
    def read(stream):
        value = StreamIO.read_byte(stream)

        return NBTTagByte(value)
