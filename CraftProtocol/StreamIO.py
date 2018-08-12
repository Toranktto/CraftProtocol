#!/usr/bin/env python

import socket
import struct


class StreamIO(object):

    @staticmethod
    def write_bool(stream, x):
        StreamIO.write_ubyte(stream, 0x01 if bool(x) else 0x00)

    @staticmethod
    def read_bool(stream):
        return True if StreamIO.read_ubyte(stream) >= 0x01 else False

    @staticmethod
    def write_byte(stream, x):
        StreamIO.write(stream, struct.pack("b", int(x)))

    @staticmethod
    def read_byte(stream):
        return struct.unpack("b", StreamIO.read(stream, 1))[0]

    @staticmethod
    def write_ubyte(stream, x):
        StreamIO.write(stream, struct.pack("B", int(x)))

    @staticmethod
    def read_ubyte(stream):
        return struct.unpack("B", StreamIO.read(stream, 1))[0]

    @staticmethod
    def write_varint(stream, x):
        x = int(x)

        if x < 0:
            x = (1 << 32) + x

        buf = ""
        while True:
            byte = x & 0x7f
            x >>= 7

            if x:
                buf += chr(byte | 0x80)
            else:
                buf += chr(byte)
                break

        StreamIO.write(stream, buf)

    @staticmethod
    def read_varint(stream):
        result = 0
        counter = 0

        while True:
            byte = StreamIO.read_byte(stream)
            result |= (byte & 0x7F) << (counter * 7)

            counter += 1
            if counter > 5:
                raise IOError("VarInt is too big")

            if not (byte & 0x80):
                break

        if result & (1 << 31):
            result = result - (1 << 32)

        return result

    @staticmethod
    def size_varint(x):
        x = int(x)

        if x < 0:
            x = (1 << 32) + x

        size = 1
        while x & ~0x7f:
            size += 1
            x >>= 7

        return size

    @staticmethod
    def write_varlong(stream, x):
        x = long(x)

        if x < 0:
            x = (1 << 32) + x

        buf = ""
        while True:
            byte = x & 0x7f
            x >>= 7

            if x:
                buf += chr(byte | 0x80)
            else:
                buf += chr(byte)
                break

        StreamIO.write(stream, buf)

    @staticmethod
    def read_varlong(stream):
        result = 0L
        counter = 0

        while True:
            byte = StreamIO.read_byte(stream)
            result |= (byte & 0x7F) << (counter * 7)

            counter += 1
            if counter > 10:
                raise IOError("VarLong is too big")

            if not (byte & 0x80):
                break

        if result & (1 << 31):
            result = result - (1 << 32)

        return result

    @staticmethod
    def size_varlong(x):
        x = long(x)

        if x < 0:
            x = (1 << 32) + x

        size = 1
        while x & ~0x7f:
            size += 1
            x >>= 7

        return size

    @staticmethod
    def write_ushort(stream, x):
        StreamIO.write(stream, struct.pack("!H", int(x)))

    @staticmethod
    def read_ushort(stream):
        return struct.unpack("!H", StreamIO.read(stream, 2))[0]

    @staticmethod
    def write_short(stream, x):
        StreamIO.write(stream, struct.pack("!h", int(x)))

    @staticmethod
    def read_short(stream):
        raw = StreamIO.read(stream, 2)
        return struct.unpack("!h", raw)[0]

    @staticmethod
    def write_int(stream, x):
        StreamIO.write(stream, struct.pack("!i", int(x)))

    @staticmethod
    def read_int(stream):
        return struct.unpack("!i", StreamIO.read(stream, 4))[0]

    @staticmethod
    def write_long(stream, x):
        StreamIO.write(stream, struct.pack("!q", long(x)))

    @staticmethod
    def read_long(stream):
        return struct.unpack("!q", StreamIO.read(stream, 8))[0]

    @staticmethod
    def write_ulong(stream, x):
        StreamIO.write(stream, struct.pack("!Q", long(x)))

    @staticmethod
    def read_ulong(stream):
        return struct.unpack("!Q", StreamIO.read(stream, 8))[0]

    @staticmethod
    def write_float(stream, x):
        StreamIO.write(stream, struct.pack("!f", float(x)))

    @staticmethod
    def read_float(stream):
        return struct.unpack("!f", StreamIO.read(stream, 4))[0]

    @staticmethod
    def write_double(stream, x):
        StreamIO.write(stream, struct.pack("!d", float(x)))

    @staticmethod
    def read_double(stream):
        return struct.unpack("!d", StreamIO.read(stream, 8))[0]

    @staticmethod
    def write_string(stream, x):
        StreamIO.write_varint(stream, len(x))
        StreamIO.write(stream, x)

    @staticmethod
    def read_string(stream):
        return StreamIO.read(stream, StreamIO.read_varint(stream))

    @staticmethod
    def write_position(stream, x, y, z):
        StreamIO.write_ulong(stream, ((x & 0x3FFFFFF) << 38) | ((y & 0xFFF) << 26) | (z & 0x3FFFFFF))

    @staticmethod
    def read_position(stream):
        val = StreamIO.read_ulong(stream)
        x = val >> 38
        y = (val >> 26) & 0xFFF
        z = val << 38 >> 38

        return x, y, z

    @staticmethod
    def write(stream, data):
        if isinstance(stream, socket._socketobject):
            return stream.send(data)

        return stream.write(data)

    @staticmethod
    def read(stream, n):
        if isinstance(stream, socket._socketobject):
            data = stream.recv(n)
            while len(data) < n:
                packet = stream.recv(n - len(data))
                if not packet:
                    stream.close()
                    raise EOFError("Unexpected EOF while reading bytes")

                data += packet

            return data

        data = stream.read(n)
        if len(data) < n:
            raise EOFError("Unexpected EOF while reading bytes")

        return data
