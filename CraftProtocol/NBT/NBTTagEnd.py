#!/usr/bin/env python

from CraftProtocol.NBT.NBTBase import NBTBase


class NBTTagEnd(NBTBase):
    TYPE_ID = 0x00

    def get(self):
        return None

    @staticmethod
    def write(stream, tag):
        pass

    @staticmethod
    def read(stream):
        return NBTTagEnd()
