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

    def __getitem__(self, key):
        return self.__values.__getitem__(key)

    def __setitem__(self, key, value):
        assert isinstance(value, NBTBase), "value must be NBTBase"

        self.__values.__setitem__(key, value)

    def __delitem__(self, key):
        self.__values.__delitem__(key)

    def __iter__(self):
        return self.__values.__iter__()

    def __contains__(self, key):
        return self.__values.__contains__(key)

    def __len__(self):
        return self.__values.__len__()

    def keys(self):
        return self.__values.keys()

    def items(self):
        return self.__values.items()

    @staticmethod
    def write(stream, tag):
        for key in tag.keys():
            StreamIO.write_ubyte(stream, tag[key].__class__.TYPE_ID)
            StreamIO.write_ushort(stream, len(key.encode("utf8")))
            StreamIO.write(stream, key.encode("utf8"))
            tag[key].__class__.write(stream, tag[key])

        StreamIO.write_ubyte(stream, NBTTagEnd.TYPE_ID)

    @staticmethod
    def read(stream):
        values = {}

        entry_type_id = StreamIO.read_ubyte(stream)
        while entry_type_id != NBTTagEnd.TYPE_ID:
            entry_name_len = StreamIO.read_ushort(stream)
            entry_name = ""
            if entry_name_len > 0:
                entry_name = StreamIO.read(stream, entry_name_len).decode("utf8")

            values[entry_name] = NBTProvider.get_tag_class(entry_type_id).read(stream)
            entry_type_id = StreamIO.read_ubyte(stream)

        return NBTTagCompound(values)
