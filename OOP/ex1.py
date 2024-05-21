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

# ______________________________________________ инициализатор (__init__)и объекты свойства (property)
# from string import ascii_letters

# class Person:
#   S_RUS = 'йцукенгшщзхъфывапролджэячсмитьбю-'
#   S_RUS_UPPER = S_RUS.upper()

#   def __init__(self, fio, ps, age, weight):
#     self.verify_fio(fio)
#     # self.verify_ps(ps)
#     # self.verify_age(age)
#     # self.verify_weight(weight)
    
#     self.__fio = fio
#     self.age = age          #|
#     self.ps = ps            #| вызываются объекты property (свойства) и в них делается проверка 
#     self.weight = weight    #| 

#   @classmethod
#   def verify_fio(cls, fio):

#     if type(fio) != str:
#       raise TypeError("ФИО должно быть строкой")
    
#     f = fio.split()
#     if len(f) != 3:
#       raise TypeError("Неверный формат ФИО")
    
#     letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

#     for s in f:
#       if len(s) < 1:
#         raise TypeError("В ФИО должен быть хотя бы один символ")
#       if len(s.strip(letters)) != 0:
#         raise TypeError("В ФИО можно использовать только буквенные символы и дефис")
      
#     print("\nФИО подтверждены")
      
#   @classmethod
#   def verify_age(cls, age):
#     if type(age) == int and 14 < age < 100:
#       print("Возраст подтверждён")
#     else:
#       raise TypeError("Возраст должен быть целым числом в диапазоне [14, 100]")
    
#   @classmethod
#   def verify_weight(cls, weight):
#     if type(weight) == float and 20 < weight < 200:
#       print("Вес подтверждён\n")
#     else:
#       raise TypeError("Вес должен быть десятичным числом в диапазоне [20, 200]")
    
#   @classmethod
#   def verify_ps(cls, ps):
#     if type(ps) != str:
#       raise TypeError("Паспорт должен быть строкой")
#     p = ps.split()
#     if len(p) != 2 or len(p[0]) != 4 or len(p[1]) != 6:
#       raise TypeError("Неверный формат паспорта. (Правильный формат: хххх хххххх, где х - это цифра)")
#     for s in p:
#       if not s.isdigit():
#         raise TypeError("Серия и номер паспорта должны быть числами")
#     print("Паспорт подтверждён")

#   @property
#   def fio(self):
#     return self.__fio
  
#   @property
#   def ps(self):
#     return self.__ps
  
#   @ps.setter
#   def ps(self, ps):
#     self.verify_ps(ps)
#     self.__ps = ps

#   @property
#   def age(self):
#     return self.__age
  
#   @age.setter
#   def age(self, age):
#     self.verify_age(age)
#     self.__age = age

#   @property
#   def weight(self):
#     return self.__weight
  
#   @weight.setter
#   def weight(self, weight):
#     self.verify_weight(weight)
#     self.__weight = weight
    

# p = Person('Hey Hello Привет', "1234 123456", 22, 68.2)

# ______________________________________________________________________________ Дискриптор
class Integer:
  @classmethod
  def verify_coord(cls, coord):
    if type(coord) != int:
      raise TypeError("")
    
  def __set_name__(self, owner, name):
    self.name = '_' + name

  def __get__(self, instance, owner):
    return getattr(instance, self.name) # ==  return instance.__dict__[self.name]
  
  def __set__(self, instance, value):
    self.verify_coord(value)
    print(f"__set__: {self.name} = {value}")
    setattr(instance, self.name, value) # ==  instance.__dict__[self.name] = value


class Point3D:
  x = Integer()
  y = Integer()
  z = Integer()

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

# _________________________________________________________________________________
