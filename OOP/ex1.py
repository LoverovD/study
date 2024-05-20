# class Point:
#   color = 'red'
#   circle = 2

#   def __init__(self, x=0, y=0):
#     self.x = x
#     self.y = y
  
#   def __del__(self):
#     print('Удаление объекта: ', str(self))
    
#   def set_cords(self, x, y):
#     self.x = x
#     self.y = y

#   def get_cords(self):
#     return(self.x, self.y)


# pt = Point(2, 5)
# print(pt.get_cords())
# _______________________________________________


# class Point:
#   def __new__(cls, *args, **kwargs):
#     print ("Вызов __new__ для " + str(cls))
#     return super().__new__(cls)

#   def __init__(self, x=0, y=0):
#     print ("Вызов __init__ для " + str(self))
#     self.x = x
#     self.y = y


# pt = Point(1, 2)
# _________________________________________________

# class Vector:
#   MIN_COORD = 0
#   MAX_COORD = 100

#   @classmethod
#   def validate(cls, arg):
#     return cls.MIN_COORD <= arg <= cls.MAX_COORD
  
#   def __init__(self, x, y):
#     self.x = self.y = 0
#     if self.validate(x) and self.validate(y):
#       self.x = x
#       self.y = y
#     print("Квадратичная норма координат: " + str(self.norm2(self.x, self.y)))
    
#   def get_coord(self):
#     return self.x, self.y
  
#   @staticmethod
#   def norm2(x, y):
#     return x*x + y*y


# v = Vector(10, 20)
# print(v.get_coord())

# ____________________________________________________________________________
# from accessify import private, protected

# class Point:
#   def __init__(self, x=0, y=0):
#     if self.__check_value(x) and self.__check_value(y):
#       self.__x = x
#       self.__y = y
#     else:
#       print("\nКоординаты должны быть числами!\nУстановлены значения по умолчанию x = 0, y = 0")
#       self.__x = 0
#       self.__y = 0

#   @private
#   @classmethod
#   def __check_value(cls, arg):
#     return type(arg) in (int, float)

#   def set_cord(self, x, y):
#     if self.__check_value(x) and self.__check_value(y):
#       self.__x = x
#       self.__y = y
#     else:
#       raise ValueError("\n\nКоординаты должны быть числами!")

#   def get_cord(self):
#     return self.__x, self.__y


# pt = Point()
# # pt.set_cord(10, 20)
# print('\n', pt.get_cord(), "\n")
# ______________________________________________________________ 7 lesson

# class Point:
#   MAX_COORD = 100
#   MIN_COORD = 0

#   def __init__(self, x=0, y=0):
#     self.x = x
#     self.y = y

#   def set_coord(self, x, y):
#     self.x = x
#     self.y = y
# _______________________________________________________________

# class Person:
#   def __init__(self, name, age):
#     self.__name = name
#     self.__age = age

#   def get_age(self):
#     return self.__age
  
#   def set_age(self, age):
#     self.__age = age

#   age = property(get_age, set_age)


# p = Person("Danik", 21)
# a = p.age
# print(a)
# p.age = 18
# print(p.age)
# print(p.__dict__)

# _____________________ == \/

# class Person:
#   def __init__(self, name, age):
#     self.__name = name
#     self.__age = age

#   @property
#   def age(self):
#     return self.__age
  
#   @age.setter
#   def age(self, age):
#     self.__age = age

#   @age.deleter
#   def age(self):
#     del self.__age


# p = Person("Danik", 21)
# a = p.age
# print(a)
# p.age = 18
# print(p.age)
# print(p.__dict__)
# del p.age
# print(p.__dict__)

# __________________________________________________________
