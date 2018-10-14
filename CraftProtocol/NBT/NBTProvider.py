#!/usr/bin/env python


class NBTProvider(object):
    _tags = {}

    @staticmethod
    def get_tag_class(type_id):
        return NBTProvider._tags[type_id]

    @staticmethod
    def register(type_id, cls):
        if type_id in NBTProvider._tags:
            raise ValueError("this tag is already registered")

        NBTProvider._tags[type_id] = cls
