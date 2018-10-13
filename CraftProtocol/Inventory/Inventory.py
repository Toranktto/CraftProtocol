#!/usr/bin/env python

from CraftProtocol.Inventory.SlotData import SlotData


class Inventory(object):

    def __init__(self, window_id, title, inventory_type, slots_number, entity_id=None):
        self.__window_id = int(window_id)
        self.__title = title
        self.__type = unicode(inventory_type)
        self.__slots = [SlotData.empty()] * int(slots_number)

        if entity_id is not None:
            entity_id = int(entity_id)

        self.__entity_id = entity_id

    @property
    def window_id(self):
        return self.__window_id

    @property
    def title(self):
        return self.__title

    @property
    def type(self):
        return self.__type

    @property
    def slots(self):
        return self.__slots

    @property
    def entity_id(self):
        return self.__entity_id

    def __getitem__(self, i):
        return self.__slots.__getitem__(i)

    def __setitem__(self, i, o):
        self.__slots.__setitem__(i, o)

    def __delitem__(self, i):
        self.__slots.__setitem__(i, SlotData.empty())

    def __len__(self):
        return self.__slots.__len__()

    def __iter__(self):
        return self.__slots.__iter__()

    def copy(self):
        inventory = Inventory(self.__window_id, self.__title, self.__type, 0, self.__entity_id)
        inventory._slots = self.__slots

        return inventory
