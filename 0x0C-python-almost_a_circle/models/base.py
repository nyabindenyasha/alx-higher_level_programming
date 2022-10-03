#!/usr/bin/python3
"""
This module contains the Base class
"""
import json
import csv
import turtle
import random


class Base():
    """Class that represents Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Method to initiate an object instance of Base"""
        self.id = id

    @staticmethod
    def reset_id():
        """Method that resets Base private attribute __nb_objects to 0"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method that takes a list of dictionaries and returns
        the JSON string representation of 'list_dictionaries'
        """

        if not list_dictionaries or list_dictionaries is None:
            ret_str = json.dumps([])
        else:
            ret_str = json.dumps(list_dictionaries, sort_keys=True)
        return(ret_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Method that returns a list of the JSON string representation
        json_string: string representing a list of dictionaries
        """
        if not json_string or json_string is None or json_string == '[]':
            return([])
        else:
            return(json.loads(json_string))

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Method that draws the objects to the screen
        """
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

        for dict_ in list_rectangles:
            for i in range(2):
                turtle.pencolor(colors[random.randint(1, 100) % 6])
                turtle.forward(dict_.width * 2)
                turtle.left(90)
                turtle.forward(dict_.height * 2)
                turtle.left(90)
            turtle.reset()

        for dict_ in list_squares:
            for i in range(4):
                turtle.pencolor(colors[random.randint(1, 100) % 6])
                turtle.forward(dict_.size * 2)
                turtle.left(90)
            turtle.reset()

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method that saves a list of dictionary objects
        as json file
        """
        data = []
        if list_objs is None:
            data = []
        else:
            for obj in list_objs:
                obj_dict = cls.to_dictionary(obj)
                data.append(obj_dict)
        fpn = '{}.json'.format(cls.__name__)
        json_data = cls.to_json_string(data)
        with open(fpn, 'w', encoding="utf-8") as fp:
            fp.write(json_data)

    @classmethod
    def load_from_file(cls):
        """
        Method that returns a list of instances loaded from a
        JSON file
        """

        try:
            with open('{}.json'.format(cls.__name__),
                      'r', encoding="utf-8") as fp:
                file_json = fp.read()
        except:
            return([])

        objects = cls.from_json_string(file_json)
        ret_list = []
        for obj in objects:
            inst_ = cls.create(**obj)
            ret_list.append(inst_)

        return(ret_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method that saves list objects to csv file"""

        data = []
        if list_objs is None:
            data = []
        else:
            for obj in list_objs:
                obj_dict = cls.to_dictionary(obj)
                data.append(obj_dict)
        fpn = '{}.csv'.format(cls.__name__)

        with open(fpn, 'w', encoding="utf-8") as cvsfile:
            if cls.__name__ == 'Rectangle':
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            else:
                fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(cvsfile, fieldnames=fieldnames)
            # writer.writeheader()
            for inst_ in data:
                writer.writerow(inst_)

    @classmethod
    def load_from_file_csv(cls):
        """
        Method that returns a list of instances loaded from a
        csv file
        """

        ret_list = []
        try:
            with open('{}.csv'.format(cls.__name__),
                      'r', encoding="utf-8") as csvfile:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                for row in reader:
                    for k, v in row.items():
                        row[k] = eval(v)
                    inst_ = cls.create(**row)
                    ret_list.append(inst_)
        except:
            pass
        return(ret_list)

    @classmethod
    def create(cls, **dictionary):
        """Method that creates an instance from a dictionary"""
        if cls.__name__ == 'Rectangle':
            r1 = cls(1, 2)
        elif cls.__name__ == 'Square':
            r1 = cls(1)
        r1.update(**dictionary)
        return(r1)

    @property
    def id(self):
        """Method to get the value of id"""
        return (self.__id)

    @id.setter
    def id(self, value):
        """Method to set the value of id"""
        if value is None:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
        else:
            self.__id = value
