from jinja2 import Template


# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value: int):
#         if len(value):
#             self.__name = value
#         else:
#             print('error name')
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if 18 <= value < 120:
#             self.__age = value
#         else:
#             print('error age')
#
#
# per = Person('Danik', 21)
# tm = Template("I'm {{p.name}} and i'm {{ p.age }} year's old.")
# msg = tm.render(p = per)
#
# print(msg)
#
# ___________________________________________________________________________

