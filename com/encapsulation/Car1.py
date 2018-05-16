#!/usr/bin/env python

class Car1:
    __maxspeed = 0                  #private variable with double underscore
    __name = ""
    __flag="true"

    def __init__(self):
        self.__maxspeed = 2001
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str (self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed


redcar = Car1()
redcar.drive ()
redcar.__maxspeed = 10  # not an eror but will not change variable because its private
redcar.drive ()

redcar.setMaxSpeed(320)
redcar.drive()
# print(redcar._Car1.__flag)