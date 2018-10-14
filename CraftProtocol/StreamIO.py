#!/usr/bin/env python

import socket
import struct


class StreamIO(object):

    @staticmethod
    def write_bool(stream, value):
        StreamIO.write_ubyte(stream, 0x01 if bool(value) else 0x00)

    @staticmethod
    def read_bool(stream):
        return True if StreamIO.read_ubyte(stream) >= 0x01 else False

    @staticmethod
    def write_byte(stream, value):
        StreamIO.write(stream, struct.pack("b", int(value)))

    @staticmethod
    def read_byte(stream):
        return struct.unpack("b", StreamIO.read(stream, 1))[0]

    @staticmethod
    def write_ubyte(stream, value):
        StreamIO.write(stream, struct.pack("B", int(value)))

    @staticmethod
    def read_ubyte(stream):
        return struct.unpack("B", StreamIO.read(stream, 1))[0]

    @staticmethod
    def write_varint(stream, value):
        value = int(value)

        if value < 0:
            value = (1 << 32) + value

        buf = ""
        while True:
            byte = value & 0x7f
            value >>= 7

            if value:
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
    def size_varint(value):
        value = int(value)

        if value < 0:
            value = (1 << 32) + value

        size = 1
        while value & ~0x7f:
            size += 1
            value >>= 7

        return size

    @staticmethod
    def write_varlong(stream, value):
        value = long(value)

        if value < 0:
            value = (1 << 32) + value

        buf = ""
        while True:
            byte = value & 0x7f
            value >>= 7

            if value:
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
    def size_varlong(value):
        value = long(value)

        if value < 0:
            value = (1 << 32) + value

        size = 1
        while value & ~0x7f:
            size += 1
            value >>= 7

        return size

    @staticmethod
    def write_ushort(stream, value):
        StreamIO.write(stream, struct.pack("!H", int(value)))

    @staticmethod
    def read_ushort(stream):
        return struct.unpack("!H", StreamIO.read(stream, 2))[0]

    @staticmethod
    def write_short(stream, value):
        StreamIO.write(stream, struct.pack("!h", int(value)))

    @staticmethod
    def read_short(stream):
        raw = StreamIO.read(stream, 2)
        return struct.unpack("!h", raw)[0]

    @staticmethod
    def write_int(stream, value):
        StreamIO.write(stream, struct.pack("!i", int(value)))

    @staticmethod
    def read_int(stream):
        return struct.unpack("!i", StreamIO.read(stream, 4))[0]

    @staticmethod
    def write_long(stream, value):
        StreamIO.write(stream, struct.pack("!q", long(value)))

    @staticmethod
    def read_long(stream):
        return struct.unpack("!q", StreamIO.read(stream, 8))[0]

    @staticmethod
    def write_ulong(stream, value):
        StreamIO.write(stream, struct.pack("!Q", long(value)))

    @staticmethod
    def read_ulong(stream):
        return struct.unpack("!Q", StreamIO.read(stream, 8))[0]

    @staticmethod
    def write_float(stream, value):
        StreamIO.write(stream, struct.pack("!f", float(value)))

    @staticmethod
    def read_float(stream):
        return struct.unpack("!f", StreamIO.read(stream, 4))[0]

    @staticmethod
    def write_double(stream, value):
        StreamIO.write(stream, struct.pack("!d", float(value)))

    @staticmethod
    def read_double(stream):
        return struct.unpack("!d", StreamIO.read(stream, 8))[0]

    @staticmethod
    def write_string(stream, value):
        StreamIO.write_varint(stream, len(value))
        StreamIO.write(stream, value)

    @staticmethod
    def read_string(stream):
        return StreamIO.read(stream, StreamIO.read_varint(stream))

    @staticmethod
    def write_position(stream, position):
        x = position[0]
        y = position[1]
        z = position[2]

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
    def read(stream, data_len):
        if isinstance(stream, socket._socketobject):
            data = stream.recv(data_len)
            while len(data) < data_len:
                packet = stream.recv(data_len - len(data))
                if not packet:
                    stream.close()
                    raise EOFError("Unexpected EOF while reading bytes")

                data += packet

            return data

        data = stream.read(data_len)
        if len(data) < data_len:
            raise EOFError("Unexpected EOF while reading bytes")

        return data
