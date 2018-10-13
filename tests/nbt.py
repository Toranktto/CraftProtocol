#!/usr/bin/env python

import unittest

import CraftProtocol


class NBTTest(unittest.TestCase):

    def test_basic(self):
        tag = CraftProtocol.NBT.NBTSerializer.read(open("tests/basic_test.nbt"))
        self.assertEqual(tag["name"].get(), "Bananrama")


if __name__ == "__main__":
    unittest.main()
