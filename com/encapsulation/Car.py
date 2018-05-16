#!/usr/bin/env python

class Car:

    def __init__(self):
        self.__updateSoftware ()

    def drive(self):
        print('driving')

    def __updateSoftware(self):             #private method(double underscore)
        print('updating software')


redcar = Car ()
redcar.drive ()
# redcar.__updateSoftware()             #not accesible from object.
redcar._Car__updateSoftware()         #makes private method visible
