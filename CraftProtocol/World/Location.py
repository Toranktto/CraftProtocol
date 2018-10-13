#!/usr/bin/env python


class Location(object):

    def __init__(self, x, y, z, yaw=0.00, pitch=0.00):
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)
        self.__yaw = float(yaw)
        self.__pitch = float(pitch)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @property
    def yaw(self):
        return self.__yaw

    @property
    def pitch(self):
        return self.__pitch

    @x.setter
    def x(self, x):
        self.__x = float(x)

    @y.setter
    def y(self, y):
        self.__y = float(y)

    @z.setter
    def z(self, z):
        self.__z = float(z)

    @yaw.setter
    def yaw(self, yaw):
        self.__yaw = float(yaw)

    @pitch.setter
    def pitch(self, pitch):
        self.__pitch = float(pitch)
