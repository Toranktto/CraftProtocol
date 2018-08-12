#!/usr/bin/env python

import gzip

import CraftProtocol


def main():
    with gzip.open("bigtest.nbt", "rb") as f:
        tag = CraftProtocol.NBT.NBTSerializer.read(f)
        value = tag["listTest (compound)"][1]["name"].get()
        if value == "Compound tag #1":
            print "OK!"
        else:
            print "FAILED!"
            print "Value = " + value


if __name__ == "__main__":
    main()
