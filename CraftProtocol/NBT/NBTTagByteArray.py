#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.StreamIO import StreamIO


class NBTTagByteArray(NBTBase):
    TYPE_ID = 0x07

    def __init__(self, values=None):
        NBTBase.__init__(self)

        if values is None:
            values = []

        self.__values = bytearray(values)

    def get(self):
        return self.__values

    def __getitem__(self, index):
        return self.__values.__getitem__(index)

    def __setitem__(self, index, value):
        self.__values.__setitem__(index, int(value))

    def __delitem__(self, index):
        self.__values.__delitem__(index)

    def __iter__(self):
        return self.__values.__iter__()

    def __contains__(self, value):
        return self.__values.__contains__(int(value))

    def __len__(self):
        return self.__values.__len__()

    def append(self, value):
        self.__values.append(int(value))

    def remove(self, value):
        self.__values.remove(int(value))

    @staticmethod
    def write(stream, tag):
        StreamIO.write_int(stream, len(tag))
        for value in tag:
            StreamIO.write_byte(stream, value)

    @staticmethod
    def read(stream):
        return NBTTagByteArray([StreamIO.read_byte(stream) for _ in xrange(StreamIO.read_int(stream))])
