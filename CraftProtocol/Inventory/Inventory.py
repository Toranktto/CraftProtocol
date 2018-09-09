#!/usr/bin/env python

from CraftProtocol.Inventory.SlotData import SlotData


class Inventory(object):

    def __init__(self, window_id, title, inventory_type, slots_number, entity_id=None):
        self._window_id = int(window_id)
        self._title = title
        self._type = unicode(inventory_type)
        self._slots = [SlotData.empty()] * int(slots_number)

        if entity_id is not None:
            entity_id = int(entity_id)

        self._entity_id = entity_id

    def get_window_id(self):
        return self._window_id

    def get_title(self):
        return self._title

    def get_type(self):
        return self._type

    def get_slots(self):
        return self._slots

    def get_entity_id(self):
        return self._entity_id

    def __getitem__(self, i):
        return self._slots.__getitem__(i)

    def __setitem__(self, i, o):
        self._slots.__setitem__(i, o)

    def __delitem__(self, i):
        self._slots.__setitem__(i, SlotData(-1))

    def __len__(self):
        return self._slots.__len__()

    def __iter__(self):
        return self._slots.__iter__()

    def copy(self):
        inventory = Inventory(self._window_id, self._title, self._type, 0, self._entity_id)
        inventory._slots = self._slots

        return inventory
