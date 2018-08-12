#!/usr/bin/env python


class NBTProvider(object):
    _TAGS = {}

    @staticmethod
    def get_tag_class(type_id):
        return NBTProvider._TAGS[type_id]

    @staticmethod
    def register(type_id, cls):
        if type_id in NBTProvider._TAGS:
            raise ValueError("This id is already registered")

        NBTProvider._TAGS[type_id] = cls
