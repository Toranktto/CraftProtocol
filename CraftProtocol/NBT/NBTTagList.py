#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.NBT.NBTProvider import NBTProvider
from CraftProtocol.StreamIO import StreamIO


class NBTTagList(NBTBase):
    TYPE_ID = 0x09

    def __init__(self, tag_type, values=None):
        NBTBase.__init__(self)

        if values is None:
            values = []

        self.__tag_type = tag_type
        self.__values = list(values)

    def get(self):
        return self.__values

    @property
    def tag_type(self):
        return self.__tag_type

    def __getitem__(self, i):
        return self.__values.__getitem__(i)

    def __setitem__(self, i, o):
        assert isinstance(o, self.__tag_type), "value must be " + self.__tag_type.__name__

        self.__values.__setitem__(i, o)

    def __delitem__(self, i):
        self.__values.__delitem__(i)

    def __iter__(self):
        return self.__values.__iter__()

    def __contains__(self, o):
        return self.__values.__contains__(o)

    def __len__(self):
        return self.__values.__len__()

    def append(self, x):
        assert isinstance(x, self.__tag_type), "arg must be " + self.__tag_type.__name__

        self.__values.append(x)

    def remove(self, x):
        assert isinstance(x, self.__tag_type), "arg must be " + self.__tag_type.__name__

        self.__values.remove(x)

    @staticmethod
    def write(stream, tag):
        StreamIO.write_ubyte(stream, tag.tag_type.TYPE_ID)
        StreamIO.write_int(stream, len(tag))

        for i in tag:
            tag.tag_type.write(stream, i)

    @staticmethod
    def read(stream):
        tag_type_id = StreamIO.read_ubyte(stream)
        tag_type = NBTProvider.get_tag_class(tag_type_id)
        values = []
        len = StreamIO.read_int(stream)

        for i in xrange(len):
            values.append(tag_type.read(stream))

        return NBTTagList(tag_type, values)
