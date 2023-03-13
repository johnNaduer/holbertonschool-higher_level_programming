#!/usr/bin/python3
"""  class Student that defines a student """

class Student:
    """ class that contains __init__ and to_json"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        mydict = {}
        data1 = 'first_name'
        data2 = 'last_name'
        data3 = 'age'
        if attrs:
            if data1 in attrs:
                mydict[data1] = self.first_name
            if data2 in attrs:
                mydict[data2] = self.last_name
            if data3 in attrs:
                mydict[data3] = self.age
            if attrs is not list:
                return self.__dict__
            return mydict
        else:
            return {'first_name':self.first_name, 'last_name': self.last_name, 'age': self.age}
