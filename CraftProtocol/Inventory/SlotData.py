#!/usr/bin/env python


class SlotData(object):

    def __init__(self, item_id, count=0, damage=0, tag=None):
        self.__id = int(item_id)
        self.__count = int(count)
        self.__damage = int(damage)
        self.__tag = tag

    @staticmethod
    def empty():
        return SlotData(-1)

    def is_empty(self):
        return self.id == -1

    @property
    def id(self):
        return self.__id

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = int(count)

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = int(damage)

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    def has_tag(self):
        return self.__tag is not None
