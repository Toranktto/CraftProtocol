#!/usr/bin/env python

__all__ = [
    "NBTBase",
    "NBTProvider",
    "NBTSerializer",
    "NBTTagByte",
    "NBTTagByteArray",
    "NBTTagCompound",
    "NBTTagDouble",
    "NBTTagFloat",
    "NBTTagInt",
    "NBTTagIntArray",
    "NBTTagList",
    "NBTTagLong",
    "NBTTagLongArray",
    "NBTTagShort",
    "NBTTagString",
    "NBTTagEnd"
]

from CraftProtocol.NBT.NBTBase import NBTBase
from CraftProtocol.NBT.NBTProvider import NBTProvider
from CraftProtocol.NBT.NBTSerializer import NBTSerializer
from CraftProtocol.NBT.NBTTagByte import NBTTagByte
from CraftProtocol.NBT.NBTTagByteArray import NBTTagByteArray
from CraftProtocol.NBT.NBTTagCompound import NBTTagCompound
from CraftProtocol.NBT.NBTTagDouble import NBTTagDouble
from CraftProtocol.NBT.NBTTagEnd import NBTTagEnd
from CraftProtocol.NBT.NBTTagFloat import NBTTagFloat
from CraftProtocol.NBT.NBTTagInt import NBTTagInt
from CraftProtocol.NBT.NBTTagIntArray import NBTTagIntArray
from CraftProtocol.NBT.NBTTagList import NBTTagList
from CraftProtocol.NBT.NBTTagLong import NBTTagLong
from CraftProtocol.NBT.NBTTagLongArray import NBTTagLongArray
from CraftProtocol.NBT.NBTTagShort import NBTTagShort
from CraftProtocol.NBT.NBTTagString import NBTTagString


def _register_tags():
    import types
    import sys

    for name, cls in sys.modules[__package__].__dict__.items():
        if isinstance(cls, types.TypeType) and issubclass(cls, NBTBase) and cls is not NBTBase:
            NBTProvider.register(cls.TYPE_ID, cls)


_register_tags()
