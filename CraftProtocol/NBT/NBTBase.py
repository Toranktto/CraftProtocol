#!/usr/bin/env python


class NBTBase(object):
    TYPE_ID = None

    def __init__(self):
        pass

    def get(self):
        return None

    @staticmethod
    def write(stream, tag):
        pass

    @staticmethod
    def read(stream):
        return NBTBase()
