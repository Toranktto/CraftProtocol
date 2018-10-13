#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.StreamIO import StreamIO


class NBTTagIntArray(NBTBase):
    TYPE_ID = 0x0B

    def __init__(self, values=None):
        NBTBase.__init__(self)

        if values is None:
            values = []

        self.__values = list(values)

    def get(self):
        return self.__values

    def __getitem__(self, i):
        return self.__values.__getitem__(i)

    def __setitem__(self, i, o):
        self.__values.__setitem__(i, int(o))

    def __delitem__(self, i):
        self.__values.__delitem__(i)

    def __iter__(self):
        return self.__values.__iter__()

    def __contains__(self, o):
        return self.__values.__contains__(int(o))

    def __len__(self):
        return self.__values.__len__()

    def append(self, x):
        self.__values.append(int(x))

    def remove(self, x):
        self.__values.remove(int(x))

    @staticmethod
    def write(stream, tag):
        StreamIO.write_int(stream, len(tag.get()))

        for i in tag.get():
            StreamIO.write_int(stream, i)

    @staticmethod
    def read(stream):
        values = []
        len = StreamIO.read_int(stream)

        for i in xrange(len):
            values.append(StreamIO.read_int(stream))

        return NBTTagIntArray(values)
