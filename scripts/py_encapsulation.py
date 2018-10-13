#!/usr/bin/env python

import re
import sys

"""
Convert Python source code with Java-style encapsulation
to Python-style properties.
"""


def main(argv):
    if len(argv) < 2:
        print "usage: python " + argv[0] + " <file>"
        sys.exit(1)

    fin = sys.stdin if argv[1] == "-" else open(argv[1], "r")

    getter_regex = re.compile("^(\s*)?def (get|is)_([A-Za-z0-9_]+)\(self\):(.*)?")
    setter_regex = re.compile("^(\s*)?def set_([A-Za-z0-9_]+)\(self, ([A-Za-z0-9_]+)\):(.*)?")
    get_regex = re.compile("^(.*)?([A-Za-z0-9_]+).(get|is)_([A-Za-z0-9_]+)\(\)(.*)?")
    set_regex = re.compile("^(.*)?([A-Za-z0-9_]+).set_([A-Za-z0-9_]+)\((.*)?\)(.*)?")

    for line in fin:
        getter_search = getter_regex.search(line)
        if getter_search:
            whitespace = getter_search.group(1)
            property_name = getter_search.group(3)
            comment = getter_search.group(4)

            sys.stdout.write(whitespace + "@property\n")
            sys.stdout.write(whitespace + "def " + property_name + "(self):" + comment + "\n")
            continue

        get_search = get_regex.search(line)
        if get_search:
            begin = get_search.group(1)
            object_name = get_search.group(2)
            property_name = get_search.group(4)
            end = get_search.group(5)

            sys.stdout.write(begin + object_name + "." + property_name + end + "\n")
            continue

        setter_search = setter_regex.search(line)
        if setter_search:
            whitespace = setter_search.group(1)
            property_name = setter_search.group(2)
            arg_name = setter_search.group(3)
            comment = setter_search.group(4)

            sys.stdout.write(whitespace + "@" + property_name + ".setter\n")
            sys.stdout.write(whitespace + "def " + property_name + "(self, " + arg_name + "):" + comment + "\n")
            continue

        set_search = set_regex.search(line)
        if set_search:
            begin = set_search.group(1)
            object_name = set_search.group(2)
            property_name = set_search.group(3)
            arg_name = set_search.group(4)
            end = set_search.group(5)

            sys.stdout.write(begin + object_name + "." + property_name + " = " + arg_name + end + "\n")
            continue

        sys.stdout.write(line)

    fin.close()


if __name__ == "__main__":
    main(sys.argv)
