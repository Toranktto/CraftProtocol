#!/usr/bin/env python


class SlotData(object):

    def __init__(self, item_id, count=0, damage=0, tag=None):
        self._id = int(item_id)
        self._count = int(count)
        self._damage = int(damage)
        self._tag = tag

    def is_empty(self):
        return self._id == -1

    def get_id(self):
        return self._id

    def get_count(self):
        return self._count

    def set_count(self, count):
        self._count = int(count)

    def get_damage(self):
        return self._damage

    def set_damage(self, damage):
        self._damage = int(damage)

    def get_tag(self):
        return self._tag

    def set_tag(self, tag):
        self._tag = tag

    def has_tag(self):
        return self._tag is not None
