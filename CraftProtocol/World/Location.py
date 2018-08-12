#!/usr/bin/env python


class Location(object):

    def __init__(self, x, y, z, yaw=0.00, pitch=0.00):
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)
        self._yaw = float(yaw)
        self._pitch = float(pitch)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def get_yaw(self):
        return self._yaw

    def get_pitch(self):
        return self._pitch

    def set_x(self, x):
        self._x = float(x)

    def set_y(self, y):
        self._y = float(y)

    def set_z(self, z):
        self._z = float(z)

    def set_yaw(self, yaw):
        self._yaw = float(yaw)

    def set_pitch(self, pitch):
        self._pitch = float(pitch)
