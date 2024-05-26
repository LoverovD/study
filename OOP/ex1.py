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
# class Integer:
#   @classmethod
#   def verify_coord(cls, coord):
#     if type(coord) != int:
#       raise TypeError("")
    
#   def __set_name__(self, owner, name):
#     self.name = '_' + name

#   def __get__(self, instance, owner):
#     return getattr(instance, self.name) # ==  return instance.__dict__[self.name]
  
#   def __set__(self, instance, value):
#     self.verify_coord(value)
#     print(f"__set__: {self.name} = {value}")
#     setattr(instance, self.name, value) # ==  instance.__dict__[self.name] = value


# class Point3D:
#   x = Integer()
#   y = Integer()
#   z = Integer()

#   def __init__(self, x, y, z):
#     self.x = x
#     self.y = y
#     self.z = z

# _____________________________________________________________________________ __call__

# class Counter:
#   def __init__(self):
#     self.__counter = 0

#   def __call__(self, *args, **kwargs):
#     print("__call__")
#     self.__counter += 1
#     return self.__counter
  

# c = Counter()
# c2 = Counter()
# c()
# c()
# c()
# print(c(), c2())

# _________________

# class Strip_Chars:
#   def __init__(self, chars: str = " "):
#     self.__chars = chars

#   def __call__(self, *args, **kwargs):
#     if not isinstance(args[0], str):
#       raise TypeError ("First argument must be str")
#     return args[0].strip(self.__chars)
  

# strip_1 = Strip_Chars(",.?!;: ")
# print(strip_1("..,Hey!?"))

# _________________ Замыкание функций
# def strip_chars(chars = ' '):
#   def do_strip(new_string):
#     return new_string.strip(chars)
#   return do_strip

# strip_1 = strip_chars()
# strip_2 = strip_chars(".,:;!? ")

# print(strip_1(" !!    Hello strip!! .   ,!!? "))
# print(strip_2("!!    Hello strip!! .   ,!!?"))

# ____________________________________________________________ dunder methods (__len__, __abs__)

# class Point:
#   def __init__(self, *args: int):
#     self.__coords = args

#   def __len__(self):
#     return len(self.__coords)
  
#   def __abs__(self):
#     return list(map(abs, self.__coords))
  

# p = Point(1, -5, 2)
# print(f"{len(p)}\n{abs(p)}")

# ___________________________________________________________ dunder methods (add, radd, iadd) 

# class Clock:
#   __DAY = 86400
#   def __init__(self, seconds: int):
#     if not isinstance(seconds, int):
#       raise TypeError("Seconds must be int value")
#     self.__seconds = seconds % self.__DAY

#   def get_time(self):
#     s = self.__seconds % 60
#     m = (self.__seconds // 60) % 60
#     h = (self.__seconds // 3600) % 24
#     print(f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}")

#   @classmethod
#   def __get_formatted(cls, x):
#     return str(x).rjust(2, '0')
  
#   def __add__(self, other):
#     if not isinstance(other, (int, Clock)):
#       raise ArithmeticError ("Right argument must be int or Clock value")
#     print("\n__add__")
    
#     sh = other
#     if isinstance(sh, Clock):
#       sh = other.__seconds

#     return Clock(self.__seconds + sh)
  
#   def __radd__(self, other):
#     print("\n__radd__")
#     return self + other
  
#   def __iadd__(self, other):
#     print("\n__iadd__")
#     return self + other
  

# time = Clock(3000) #  50 min
# time += 3000
# time_2 = Clock(1500) #  25 min
# time.get_time()
# time += time_2
# time.get_time()
# time = (-3000) + time
# time.get_time()

# __________________________________________________________________ dunder methods (getitem, setitem)

# class Student:
#   def __init__(self, name: str, marks: list):
#     self.name = name
#     self.marks = list(marks)

#   def __getitem__(self, number):
#     if 0 <= number < len(self.marks):
#       return self.marks[number]
#     else:
#       raise IndexError ("\n\nInvaild index")
    
#   def __setitem__(self, number, value):
#     if not isinstance(value, int) or (10 < value < 0):
#       raise ValueError ("\n\nThe value of mark must be int [0, 10]")
#     if number < 0:
#       raise IndexError('Index < 0 out of range')
#     if number >= len(self.marks):
#       off = number + 1 - len(self.marks) 
#       self.marks.extend([None]*off)
    
#     self.marks[number] = value
#     print(f"Value marks[{number}] is changed to {value}")
    
      
  
#   def __delitem__(self, number):
#     if 0 <= number < len(self.marks):
#       del(self.marks[number])
#       print(f"Value marks[{number}] is deleted")
#     else:
#       raise IndexError ("\n\nInvaild index")


# student_1 = Student('Daniil', [5, 5, 3, 1, 6, 6,])
# print(f"\n{student_1.marks}")
# print(f"old value = {student_1[0]}\n")
# student_1[0] = 0
# print(f"\n{student_1.marks}")
# print(f"changed value = {student_1[0]}\n")
# del(student_1[0])
# print(f"\n{student_1.marks}")
# print(f"new value with [0] index = {student_1[0]}\n")
# student_1[10] = 6
# print(f"{student_1.marks}\n")

# ________________________________________________________________________  Наследование

# class Geom:
#   def __init__(self, x1: int=0, x2: int=0, y1: int=0, y2: int=0):
#     self._x1 = x1
#     self._x2 = x2
#     self._y1 = y1
#     self._y2 = y2

#   def search_pr(self):
#     raise IndentationError(f"{self.__name__} _search_pr method needs to be overridden")
  
#   def draw_figure(self):
#     print(f"{self.__class__} _draw_figure method needs to be overridden")

# class Rectangle(Geom):
#   def __init__(self, x1, x2):
#     super().__init__(x1, x2)

#   def search_pr(self):
#     return (self._x1+self._x2)*2
  
#   def draw_figure(self):
#     print("Drawing rectangle")
  
# class Square(Geom):
#   def __init__(self, x1):
#     super().__init__(x1)

#   def search_pr(self):
#     return (self._x1*4)


# geom = [ Rectangle(1, 2),
# Rectangle(5, 6),
# Square(2),
# Square(4)
# ]

# for g in geom:
#   print(f"\n{g.search_pr()}")
#   g.draw_figure()

# _______________________________________________________________ super()

# class Goods:
#   def __init__(self, name: str = "Noname", price: int = 0, weight: float = 0.0):
#     super().__init__()
#     self._name = name
#     self._price = price
#     self._weight = weight
#     print("Goods __init__")

#   def print_info(self):
#     print(f"\nname: {self._name}\nprice: {self._price}\nweight: {self._weight}\n")

# class Sales_ID:
#   ID = 1

#   def __init__(self):
#     self._id = self.ID
#     self.ID += 1
#     print("Sales_ID __init__")

#   def print_info(self):
#     print(f"id of sales operation is {self._id}")

# class NoteBook(Goods, Sales_ID):
#   def print_id(self):
#     Sales_ID.print_info(self)


# print(f"\nПорядок наследований и вызова функций super() класса NoteBook: {NoteBook.__mro__}\n\n")
# n1 = NoteBook("Asr", 3000, 1.2)
# n2 = NoteBook("Asus", 40000, 5.5)
# n1.print_info()
# n1.print_id()
# n2.print_info()
# n2.print_id()

# ______________________________________________________ __slots__ and property при наследовании

# class Point2D:
#   __slots__ = ('_x', '_y', '_lenth')

#   def __init__(self, x: int = 0, y: int = 0):
#     self._x = x
#     self._y = y
#     self._lenth = (x+x)*(y+y)
#     print("Point2D __init__")

#   @property
#   def lenth(self):
#     print(f"{self._lenth}\n")
#     return self._lenth
  
#   @lenth.setter
#   def lenth(self, value):
#     self._lenth = value
#     print(f"_lenth = {value}")
    


# class Point3D(Point2D):
#   __slots__ = '_z',

#   def __init__(self, x: int = 0, y: int = 0, z: int = 0):
#     super().__init__(x, y)
#     self._z = z
#     self._lenth = (int(self._lenth) * (z+z))
#     print("Point3D __init__")

  
# p3 = Point3D(1, 2, 2)
# p3.lenth
# p2 = Point2D(1, 2)
# p2.lenth
# p2.lenth = 100
# p2.lenth

# ________________________________ различия __slots__ и __dict__



# import timeit

# class Point:

#   def __init__(self, x: int = 0, y: int = 0):
#     self._x = x
#     self._y = y
#     print("Point __init__")

#   def calc(self):
#     self._x +=1
#     del self._y
#     self._y = 0


# class Point_slots:
#   __slots__ = ('_x', '_y')

#   def __init__(self, x: int = 0, y: int = 0):
#     self._x = x
#     self._y = y
#     print("Point_slots __init__")

#   def calc(self):
#     self._x +=1
#     del self._y
#     self._y = 0

  
# p1 = Point(1, 2)
# p2 = Point_slots(1, 2)
# print(f"\nОбъём занимаемой памяти объекта класса с __dict__ = {p1.__sizeof__() + p1.__dict__.__sizeof__()}")
# print(f"Объём занимаемой памяти объекта класса с __slots__ = {p2.__sizeof__()}\n")

# t1 = timeit.timeit(p1.calc)
# t2 = timeit.timeit(p2.calc)
# print(f"\nСкорость реализации объекта класса с __dict__ = {t1}")
# print(f"Скорость реализации объекта класса с __slots__ = {t2}\n")

# ________________

# import timeit

# rows = 5
# cols = 10

# def calc_short_top():
#   iterations = 0
#   for i in range(rows):
#     for j in range(cols):
#       iterations += 1
#   return iterations

# def calc_long_top():
#   iterations = 0
#   for i in range(cols):
#     for j in range(rows):
#       iterations += 1
#   return iterations


# short_time = timeit.timeit(calc_short_top)
# long_time = timeit.timeit(calc_long_top)

# print((short_time, long_time))

# ___________________________________________________________ Exception

# class PrintError(Exception):
#   """ Общий класс исключений принтера """


# class PrintSendDataError(PrintError):
#   """ Класс исключений при отправке данных принтеру """
#   def __init__(self, *args):
#     self._message = args[0] if args else None

#   def __str__(self):
#     print(f"Ошибка: {self._message}")


# class PrintData:
#   def print(self, data):
#     self.send_data(data)
#     print(f"Печать: {str(data)}")

#   def send_data(self, data):
#     if not self.send_to_print(data):
#       raise PrintSendDataError("принтер не отвечает")

#   def send_to_print(self, data):
#     if data:
#       return True
#     else:
#       return False


# p = PrintData()
# p.print('')

# _____________________________________________________________________ Работа с файлами

# fp = None
# try:
#   fp = open("README.txt")
#   for f in fp:
#     print (f)
# except Exception as e:
#   print(e)
# finally:
#   if fp is not None:
#     fp.close()

# ________________________ Менеджер контекста

# fp = None
# try:
#   with open("README.txt") as fp:
#     for f in fp:
#       print (f)
# except Exception as e:
#   print(e)

# ________________________
# class DefendVector:
#   def __init__(self, vector):
#     self.__v = vector

#   def __enter__(self):
#     self.__temp = self.__v[:] # создаём копию вектора, что бы не изменять его в случае возникновения ошибок
#     return self.__temp
  
#   def __exit__(self, exc_type, exc_val, exc_tb):
#     if exc_type is None:
#       self.__v[:] = self.__temp

#       return False # когда exit возвращает False ошибки не обрабатываются внутри менеджера контекста

# v1 = [1, 2, 3, 4]
# v2 = [2, 3, 4]

# try:
#   with DefendVector(v1) as dv:
#     for i, value_trash in enumerate(dv): # перебирает элементы dv (возвращает индекс (i) и значение (value_))
#       dv[i] += v2[i]
# except:
#   print("Error")

# print(v1)

# ____________________________________________________________ Data Classes

# from dataclasses import dataclass, field, InitVar
# # функция field позволяет тонко настраивать поведение атрибутов
# @dataclass
# class V3D:
#   x: int = 0
#   y: int = 0
#   z: int = 0
#   calc_len: InitVar[bool] = True # параметр аннотированный InitVar автоматически передаётся в __post_init__
#   lenth: float = field(init=False, default=0) # убирает параметр из инициализатора

#   def __post_init__(self, calc_len: bool):
#     if calc_len:
#       self.lenth = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


# v = V3D(2, 3, 2)
# print(v)
# v_false = V3D(2, 3, 2, False)
# print(v_false)

# ____________________________________________________________________________________________________________
