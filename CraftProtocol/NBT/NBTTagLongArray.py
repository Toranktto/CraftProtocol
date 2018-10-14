#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.StreamIO import StreamIO


class NBTTagLongArray(NBTBase):
    TYPE_ID = 0x0C

    def __init__(self, values=None):
        NBTBase.__init__(self)

        if values is None:
            values = []

        self.__values = list(values)

    def get(self):
        return self.__values

    def __getitem__(self, index):
        return self.__values.__getitem__(index)

    def __setitem__(self, index, value):
        self.__values.__setitem__(index, long(value))

    def __delitem__(self, index):
        self.__values.__delitem__(index)

    def __iter__(self):
        return self.__values.__iter__()

    def __contains__(self, value):
        return self.__values.__contains__(long(value))

    def __len__(self):
        return self.__values.__len__()

    def append(self, value):
        self.__values.append(long(value))

    def remove(self, value):
        self.__values.remove(long(value))

    @staticmethod
    def write(stream, tag):
        StreamIO.write_long(stream, len(tag))
        for value in tag:
            StreamIO.write_long(stream, value)

    @staticmethod
    def read(stream):
        return NBTTagLongArray([StreamIO.read_long(stream) for _ in xrange(StreamIO.read_long(stream))])
