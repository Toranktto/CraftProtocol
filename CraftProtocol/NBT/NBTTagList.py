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

        self._tag_type = tag_type
        self._values = list(values)

    def get(self):
        return self._values

    def get_tag_type(self):
        return self._tag_type

    def __getitem__(self, i):
        return self._values.__getitem__(i)

    def __setitem__(self, i, o):
        assert isinstance(o, self._tag_type), "object arg must be " + self._tag_type.__name__

        self._values._setitem__(i, o)

    def __delitem__(self, i):
        self._values.__delitem__(i)

    def __iter__(self):
        return self._values.__iter__()

    def __contains__(self, o):
        return self._values.__contains__(o)

    def __len__(self):
        return self._values.__len__()

    def append(self, x):
        assert isinstance(x, self._tag_type), "x arg must be " + self._tag_type.__name__

        self._values.append(x)

    def remove(self, x):
        assert isinstance(x, self._tag_type), "x arg must be " + self._tag_type.__name__

        self._values.remove(x)

    @staticmethod
    def write(stream, tag):
        StreamIO.write_ubyte(stream, tag.get_tag_type().TYPE_ID)
        StreamIO.write_int(stream, len(tag))

        for i in tag:
            tag.get_tag_type().write(stream, i)

    @staticmethod
    def read(stream):
        tag_type_id = StreamIO.read_ubyte(stream)
        tag_type = NBTProvider.get_tag_class(tag_type_id)
        values = []
        len = StreamIO.read_int(stream)

        for i in xrange(len):
            values.append(tag_type.read(stream))

        return NBTTagList(tag_type, values)
