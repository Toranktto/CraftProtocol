#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.NBT.NBTProvider import NBTProvider
from CraftProtocol.NBT.NBTTagEnd import NBTTagEnd
from CraftProtocol.StreamIO import StreamIO


class NBTTagCompound(NBTBase):
    TYPE_ID = 0x0A

    def __init__(self, values=None):
        NBTBase.__init__(self)

        if values is None:
            values = {}

        self.__values = dict(values)

    def get(self):
        return self.__values

    def __getitem__(self, k):
        return self.__values.__getitem__(k)

    def __setitem__(self, k, v):
        assert isinstance(v, NBTBase), "value must be NBTBase"

        self.__values.__setitem__(k, v)

    def __delitem__(self, k):
        self.__values.__delitem__(k)

    def __iter__(self):
        return self.__values.__iter__()

    def __contains__(self, k):
        return self.__values.__contains__(k)

    def __len__(self):
        return self.__values.__len__()

    def keys(self):
        return self.__values.keys()

    def items(self):
        return self.__values.items()

    @staticmethod
    def write(stream, tag):
        for i in tag.keys():
            StreamIO.write_ubyte(stream, tag[i].__class__.TYPE_ID)
            StreamIO.write_ushort(stream, len(i.encode("utf8")))
            StreamIO.write(stream, i.encode("utf8"))
            tag[i].__class__.write(stream, tag[i])

        StreamIO.write_ubyte(stream, NBTTagEnd.TYPE_ID)

    @staticmethod
    def read(stream):
        values = {}
        entry_type_id = StreamIO.read_ubyte(stream)

        while entry_type_id != NBTTagEnd.TYPE_ID:
            entry_name_len = StreamIO.read_ushort(stream)
            entry_name = u""
            if entry_name_len > 0:
                entry_name = StreamIO.read(stream, entry_name_len).decode("utf8")

            entry_type = NBTProvider.get_tag_class(entry_type_id)
            values[entry_name] = entry_type.read(stream)

            entry_type_id = StreamIO.read_ubyte(stream)

        return NBTTagCompound(values)
