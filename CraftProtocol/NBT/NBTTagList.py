#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.NBT.NBTProvider import NBTProvider
from CraftProtocol.StreamIO import StreamIO


class NBTTagList(NBTBase):
    TYPE_ID = 0x09

    def __init__(self, tag_class, values=None):
        NBTBase.__init__(self)

        if values is None:
            values = []

        self.__tag_class = tag_class
        self.__values = list(values)

    def get(self):
        return self.__values

    @property
    def tag_class(self):
        return self.__tag_class

    def __getitem__(self, index):
        return self.__values.__getitem__(index)

    def __setitem__(self, index, value):
        assert isinstance(value, self.__tag_class), "value must be " + self.__tag_class.__name__

        self.__values.__setitem__(index, value)

    def __delitem__(self, index):
        self.__values.__delitem__(index)

    def __iter__(self):
        return self.__values.__iter__()

    def __contains__(self, value):
        return self.__values.__contains__(value)

    def __len__(self):
        return self.__values.__len__()

    def append(self, value):
        assert isinstance(value, self.__tag_class), "arg must be " + self.__tag_class.__name__

        self.__values.append(value)

    def remove(self, value):
        assert isinstance(value, self.__tag_class), "arg must be " + self.__tag_class.__name__

        self.__values.remove(value)

    @staticmethod
    def write(stream, tag):
        StreamIO.write_ubyte(stream, tag.tag_class.TYPE_ID)
        StreamIO.write_int(stream, len(tag))
        for value in tag:
            tag.tag_class.write(stream, value)

    @staticmethod
    def read(stream):
        tag_class = NBTProvider.get_tag_class(StreamIO.read_ubyte(stream))
        return NBTTagList(tag_class, [tag_class.read(stream) for _ in xrange(StreamIO.read_int(stream))])
