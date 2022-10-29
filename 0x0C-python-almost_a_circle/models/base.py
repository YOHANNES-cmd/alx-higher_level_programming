#!/usr/bin/python3
"""The Base module"""
import json
from os import path
import csv
import turtle as t
from random import choice


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return str representation of list_dict"""
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a fil"""
        if not list_objs:
            list_objs = []
        list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8")\
                as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """return dict representation of json_string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create base instance from dictionnary"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """create objects from json strings in file"""
        file_load = "{}.json".format(cls.__name__)
        if not path.isfile(file_load):
            return []
        with open(file_load, "r", encoding="utf-8")\
                as file:
            return[cls.create(**dic) for dic in
                   cls.from_json_string(file.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the csv string representation of list_objs to a fil"""
        if not list_objs:
            list_objs = []
        with open("{}.csv".format(cls.__name__), "w", encoding="utf-8")\
                as file:
            if cls.__name__ == "Rectangle":
                fields = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fields = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(file, fieldnames=fields)
            for ob in list_objs:
                writer.writerow(ob.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """create objects from csv strings in file"""
        list_objs = []
        with open("{}.csv".format(cls.__name__), 'r') as file:
            if cls.__name__ == "Rectangle":
                fields = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fields = ['id', 'size', 'x', 'y']
            reader = csv.DictReader(file, fieldnames=fields)
            list_objs = []
            for row in reader:
                for key in row:
                    row[key] = int(row[key])
                list_objs.append(cls.create(**row))
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws rectangles and squares"""
        t.color("white")
        r = ["gray", "blue", "yellow", "purple", "red", "green", "brown"]
        t.goto(-300, 300)

        def rec(col, lon, lar):
            t.pendown()
            t.pensize(1)
            t.color(col)
            t.begin_fill()
            for i in range(0, 2):
                t.forward(lon)
                t.right(90)
                t.forward(lar)
                t.right(90)
            t.penup()
            t.end_fill()

        for i in list_rectangles:
            rec(choice(r), i.width, i.height)
            t.forward(i.width)
            t.color('white')
            t.forward(10)
        for i in list_squares:
            rec(choice(r), i.size, i.size)
            t.forward(i.size)
            t.color('white')
            t.forward(10)
        t.exitonclick()
