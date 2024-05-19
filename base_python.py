# def IsPrime(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n
#
#
# print (IsPrime(8))


# ____________________________________________________________________
# my_list = [3, 2.5, 'a', "bc", True]
# print(len(my_list),'\n')
#
# deleted_element = my_list.pop(2)
# print(len(my_list), '| deleted element is ', deleted_element,'\n')
#
# my_list.reverse()  # поменять порядок элементов в списке
# my_list.pop(2)
# my_list.sort()
# print(my_list, '\n')
#
# new_list = ['hey', 'buy']
# my_list.extend(new_list)
# print(my_list, '\n')


# _______________________________________
# first_list = [1, 2, 3]
# second_list = [5, 6]
# full_list = first_list + second_list
# print (full_list)
# print(first_list.__add__(second_list))


#_________________________________________ СЛОВАРИ
# my_dict = {
#     'num': 12,
#     'name': 'danik',
#     'age': 22
# }
# print(my_dict)
# print(my_dict['name'])
# print(my_dict['age'], '\n')
#
# my_dict['num'] = 1
# print('new number is ', my_dict['num'], '\n')
#
# print('длинна старого словаря: ', len(my_dict))
# my_dict['surname'] = 'loverov'
# print('словарь в новой переменной:\n', my_dict)
# print('длинна нового словаря: ', len(my_dict), '\n')
#
# del my_dict['num']
# print('длинна словаря после удаления 1го эл.: ', len(my_dict))
# print(my_dict)


# __________________________________________________________________ переменные в словарях
# my_dict = {
#     'num': 12,
#     'name': 'danik',
#     'age': 22
# }
#
# key_name = 'name'
# print(key_name)
# print('old result: ', my_dict['name'])
#
#
# my_dict[key_name] = 'nikita'
# print('new result: ', my_dict['name'], '\n')


# _________________________________________________________________________Словари
# def input_dict():
#     new_key = input('enter a key: ')
#     new_volume = input('enter a volume: ')
#     return new_key, new_volume
#
#
# my_list = {}
# for i in range(3):
#     new_key, new_volume = input_dict()
#     my_list[str(new_key)] = new_volume
#
# print(my_list)


# ____________________________________________________________________________
# my_set = {1, 1, 2, 3}
# print(my_set)
# print(len(my_set), '/n')
#
# my_set.add(5)
# print(my_set)
# print(len(my_set), '\n')
#
# other_set = {'a', 'b', 1, 1}
# union_set = my_set.union(other_set)  # объединение наборов
# print(union_set)
# print(len(union_set), '\n')
#
# union_set = my_set | other_set
# print(union_set)
# print('union set: ', len(union_set), '\n\n')
#
#
# intersection_set = my_set.intersection(other_set)  # пересечение
# print(intersection_set, '\n', len(intersection_set))
# intersection_set = my_set & other_set
# print(intersection_set, '\n', len(intersection_set), '\n')
#
# print(other_set.intersection('abc'))
# print(other_set.intersection(['a', 'c', 'd']), '\n\n')
#
#
# nums = {10, 5, 35}
# other_nums = {20, 10, 5, 35, 40}
# res = nums.issubset(other_nums)  # проверка включён один набор в другой или нет (явлиется ли множество nums подмножеством множества other_nums)
# print(res)
# print(other_nums.issuperset(nums), '\n\n')  # наоборот
#
#
# my_set = {'a', 'b', 'c'}
# print('new set:\n', my_set, '\n', len(my_set), '\n')  # удаление элементов из набора
# my_set.discard('a')  # + метод remove()
# print('after deleted (a):\n', my_set, '\n', len(my_set), '\n')
#
# copied_set = my_set.copy()
# print('copied set: ', copied_set, '\n')
# my_set.add('z')
# copied_set.add('x')
# print('my_set ', my_set, '\ncopied_set ', copied_set, '\n\n')
#
# print(my_set.symmetric_difference(copied_set), '  эдементы которых нет в пересечении множеств\n')
# print((my_set | copied_set) - (my_set & copied_set), '  тоже самой формулой\n\n')
#
#
# ____________________________________________________________________________ задача по наборам
# my_set = {1, 2, 3, 4}
# my_set.add(5)
# new_set = {4, 5, 6, 7}
# common_el = list(my_set & new_set)  # можно использовать метод intersected()
# print('my_set: ', my_set, '\nnew_set: ', new_set, '\ncommon elements (list): ', common_el)
#
#
# _______________________________________________________________________________функция zip
# fruits = ['apple', 'banana', 'lime']
# quantities = [100, 70, 50]
# availability = [True, False, True, True]
#
# goods = zip(fruits, quantities, availability)
# print('list: ', list(goods))
#
# goods_dict = dict(zip(fruits, quantities))
# print('dict: ', goods_dict)


# ____________________________________________________________________________________
# info = {
#     'name': 'Danik',
#     'feels': 'good',
#     'age': 10,
#     'list': []
# }
#
# info_copy = info.copy()  # функция copy() создаёт* копию изменяемого объекта в памяти, но только 1 ур.
# print('info: ', id(info), ' // ', info, '\ninfo_copy: ', id(info_copy), ' // ', info_copy, '\n')
#
# info_copy['age'] = 21  # если в копии изменить неизменяемый объект, то оригинал не измениться
# print('info: ', id(info), ' // ', info, '\ninfo_copy: ', id(info_copy), ' // ', info_copy, '\n')
#
# info_copy['list'].append('new list el')  # если есть вложенный изменяемый объект, то он измениться и в копии и в оригинале
# print('info: ', id(info), ' // ', info, '\ninfo_copy: ', id(info_copy), ' // ', info_copy, '\n')

# ____________________________________________ как избежать изменения копий
# from copy import deepcopy
#
# info = {
#     'name': 'Danik',
#     'feels': 'good',
#     'age': 10,
#     'list': []
# }
#
# info_deepcopy = deepcopy(info)  # создание полной копии словаря (с созданием копий вложенных изменяемых объектов)
#
# info_deepcopy['list'].append('new list el')
# print('info: ', id(info), ' // ', info, '\ninfo_deepcopy: ', id(info_deepcopy), ' // ', info_deepcopy, '\n')


# ______________________________________________________________________________________________________________________ ФУНКЦИИ
# изменяемые параметры функции
# def increase_person_age(person):  # переданный в функцию изменяемый параметр, изменяет и внешний аргумент
#     print(id(person))
#     person['age'] += 1
#     return person
#
#
# person_one = {
#     'neme': 'Danik',
#     'age': 12
# }
#
# print(id(person_one))
# increase_person_age(person_one)
# print(person_one['age'])
# _________________________________________
# как избежать изменения внешних переменных
# def increase_person_age(person):
#     person_copy = person.copy()
#     print('person_copy id: ', id(person_copy))
#     person_copy['age'] += 1
#     return person_copy
#
#
# person_one = {
#     'neme': 'Danik',
#     'age': 12
# }
#
# print('person id: ', id(person_one))
# person_copy = increase_person_age(person_one)
# print('person age: ', person_one['age'], '\nperson_copy age: ', person_copy['age'])


# _____________________________________________________________________________________ TASK
# def merge_lists_to_dict(first_list, second_list):
#     return dict(zip(first_list, second_list))
#
#
# names = ['danik', 'nikita', 'oth']
# ages = [11, 5, 77]
# print(merge_lists_to_dict(names, ages))
#
#
# _____________________________________________________________________________________ обработка функцией разного кол-ва параметров
# def sum_nums(*args):  #как параметр функция примет tuple
#     print(type(args), '| ', args)
#     return sum(args)
#
#
# print(sum_nums(1, 2, 3, 4, 5), '\n')
# print(sum_nums())


# ____________________________________________________________________________________ аргументы с ключевыми словами
# def get_posts_info(name, posts_qty):
#     inf = f"{name} wrote {posts_qty} posts"
#     return inf
#
#
# info = get_posts_info(posts_qty=21, name='Danik')
# print(info)


# ___________________________________________________________________________________
# def get_posts_info(**person):  #как параметр функция примет dict
#     print('(dict) параметры: ', person)
#     inf = f"{person['name']} wrote {person['posts_qty']} posts"
#     return inf
#
#
# info = get_posts_info(posts_qty=21, name='Danik')
# print(info)
#
#
# ___________________________________________________________________________________ Задачи функции
# def merge_lists_to_dict(first_list, second_list):
#     return dict(zip(first_list, second_list))
#
#
# names = ['danik', 'nikita', 'oth']
# ages = [11, 5, 77]
# print(merge_lists_to_dict(first_list=names, second_list=ages))
# print(merge_lists_to_dict(names, second_list=ages))
#
#
# def update_car_info(**car):
#     car['is_available'] = True
#     return car
#
#
# print('\n', update_car_info(brand='BMW', price=37000))
#
#
# _____________________________________________________________________________
# from datetime import date
#
#
# def get_weekday():
#     return date.today().strftime('%A')
#
#
# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['created_on_weekday'] = weekday
#     return post_copy
#
#
# initials_posts = {'id': 342, 'author': 'Danik'}
# print(create_new_post(initials_posts))
#
#
# ______________________________________________________________________________
# def print_num_info(num):
#     if (num % 2) == 0:
#         print("entered number is even")
#     else:
#         print("entered number is odd")
#
#
# def print_square_num(num):
#     print("square of num is: ", num * num)
#
#
# def process_num_info(num, callback_fn):
#     callback_fn(num)
#
#
# extended_num = int(input('enter any number: '))
# process_num_info(extended_num, print_num_info)
# process_num_info(extended_num, print_square_num)


# ______________________________________________________________
# a = 5
#
#
# def fn_one():
#     def fn_two():
#         def fn_three():
#             def fn_four():
#                 print(a)
#             fn_four()
#         global b  # create global b in function
#         b = 10
#         fn_three()
#     fn_two()
#
#
# fn_one()
# print(b)
#
#
# _______________________________________________________________________
# set_one = {1, 2, 3, 4}
# set_two = {4, 3, 2, 1}
#
# print(set_one == set_two)
# print(set_one is set_two)
# print(id(set_one) == id(set_two))
# print(5 in set_one, 4 in set_two)
#
#
# ________________________________________________________________________
# dict_1 = {'name': 'danik', 'age': 12}
# dict_2 = dict_1.copy()
# # dict_2['name'] = 'nikita'
# (dict_1 == dict_2) and print('dicts are iqual')
#
#
# ________________________________________________________________________ распаковка и объединение словарей
# pm_info = {
#     'name': 'PYT',
#     'author': 'danik',
# }
# pm_style = {
#     'color': 'black',
#     'size': '200x400',
# }
# pm_functions = {
#     'info': "gives u information",
#     'metod': "doing smth",
# }
#
# pm_dict1 = {
#     **pm_info,  # объединение словарей с помощью распаковки (**)
#     **pm_style,
#     **pm_functions
# }
# print(pm_dict1)
#
# pm_dict2 = pm_functions | pm_info | pm_style  # объединение словарей с помощью оператора |
# print(pm_dict2)
#
#
# ____________________________________________________________________________ lambda functions
# def greeting(greet):
#     return lambda name: f"{greet}, {name}"
#
#
# morning_greeting = greeting("Good morning")
# print(morning_greeting('Danik'))
#
# evening_greeting = greeting("Good evening")
# print(evening_greeting('Nikita'))
#
# afternoon_greeting = greeting("Good afternoon")
# print(afternoon_greeting('Bogdan'))
#
#
# _________________________________________________________________________ try, except - обработка ошибок
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Division by zero!")
#
# print('Continue... ')
# ______________________________
# try:
#     print(10 / 0)
# except ZeroDivisionError as e:
#     print(e)
#     print(type(e))
#     print(dir(e))
#
# print('Continue... ')
# ______________________________
# try:
#     print('10' / 0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
#
# print('Continue... ')
# ______________________________
# try:
#     print(5 / 1)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:  # выполняется если в блоке try небыло ошибок
#     print("There was no error")
# finally:  # выполняется в любом случае
#     print('Continue... ')
# ______________________________
# try:
#     print('4' / 0)
# except Exception as e:
#     print(e)
# ______________________________
# def divide_nums(a, b):
#     if b == 0:
#         raise TypeError("Second argument can't be 0")  # raise генерирует ошибку определнного типа
#     return a / b
#
#
# try:
#     divide_nums(5, 0)
# except TypeError as e:
#     print(e)
# finally:
#     print('Continue...')
# ______________________________ задача по ошибкам try except
# def image_info(info: dict):
#     if type(info) != type(dict()):
#         raise TypeError("Function image_info accepts dict() args...")
#     else:
#         if 'image_title' and 'image_id' in info:
#             return f"Image {info['image_title']} has id {info['image_id']}"
#         else:
#             raise TypeError("One of required keys is absent (image_title or image_id)")
#
#
# image_1 = {
#     'image_title': 'Cat',
#     'image_id': 2231
# }
# image_2 = {
#     'image_tittle': 'Dog',
# }
# image_3 = 334
# try:
#     print(image_info(image_3))
# except TypeError as e:
#     print(e)
# finally:
#     print('Continue... ')

# ______________________________  #распаковка словаря в функцию
# def user_info(name, comments_qty=0):
#     if not comments_qty:
#         return f"{name} has no comments"
#     return f"{name} has {comments_qty} comments"
#
#
# user_profile = {
#     'name': 'Danik',
#     'comments_qty': 31,
# }
#
# print(user_info(**user_profile))  # == print(user_info(user_profile['name'], user_profile['comments_qty']))
# ______________________________ задача по распаковке списка словарей
# def get_info(name, age=0):
#     if not age:
#         return f"{name} hasn't indicated age"
#     return f"{name} is {age} years old"
#
#
# persons = [{'name': 'Danik', 'age': 21}, {'name': 'Nikita', 'age': 19}, {'name': 'Chel'}]
# pers_1, pers_2, pers_3 = persons
# print(get_info(**pers_1), '\n')
# print(get_info(**pers_2), '\n')
# print(get_info(**pers_3), '\n')

# ______________________________ задача условные инструкции
# def route_info(info: dict()):
#     if type(info) is not dict:
#         return f"Error, enter dict"
#     if info.get('distance') and (type(info['distance']) is int):
#         return f"Distance to ur destination is {info['distance']}"
#     if info.get('speed') and info.get('time') and (type(info['speed']) is int) and (type(info['time']) is int):
#         return f"Distance to ur destination is {info['speed'] * info['time']}"
#     return f"No distance info is available"
#
#
# print(route_info({'distance': 12}))
# print(route_info({'speed': 5, 'time': 3}))
# print(route_info({'stance': 12}))
# print(route_info(2))
# ______________________________ тернарный оператор
# product_qty = 0
# print("in stock" if product_qty > 0 else "out of stock")
#
# temp = +24
# weather = f"Weather is {'hot' if temp > 18 else 'cold'}"
# print(weather)
#
# string = "12345678910"
# print('string is long' if len(string) > 10 else 'string is short')
# ______________________________ циклы
#
# my_dict = {'id': 12321, 'title': 'test'}  # как в цикле for in со словарём получить доступ сразу к ключу и значению
#
# for item in my_dict.items():  # словарь разбивается на кортежи
#     key, value = item  # распаковка кортежей поэлементно
#     print('kye:', key, '| value:', value)
# # ______________________________
# my_dict = {'id': 12321, 'title': 'test'}  # как в цикле for in со словарём получить доступ сразу к ключу и значению
#
# for key, value in my_dict.items():  # словарь разбивается на кортежи и сразу распаковывается
#     print('kye:', key, '| value:', value)
# ______________________________
# def dict_to_list(dictt: dict):
#     list_of_tuples = []
#     for key, value in dictt.items():
#         if type(value) is int:
#             value = value * 2
#         list_of_tuples.append((key, value))
#     return list_of_tuples
#
#
# heg = {
#     'id': 123,
#     'title': 'hello',
#     'age': 12,
#     'gggh': True
# }
# print(dict_to_list(heg))
# ______________________________
# def filter_list(ful_list, typ):
#     if typ not in (int, float, bool, str, list, dict, tuple, set):
#         return f"incorrect type"
#     new_list = []
#     for el in ful_list:
#         if type(el) is typ:
#             new_list.append(el)
#     return new_list
#
#
# my_list = [1, 2, 'ffg', True, 1.2, 6]
# print(filter_list(my_list, int))
# ______________________________
# def filter_list(list_to_filter, value_type):  # функция filter
#     return list(filter(lambda elem: type(elem) is value_type, list_to_filter))
#
#
# res = filter_list([1, 2, 'ffg', True, 1.2, 6], int)
# print(res)
# ______________________________ цикл while (continue, break)
# import random
#
# random_num = random.randint(1, 5)
#
# while True:
#     num = int(input('number 1 - 5 | '))
#     if num != random_num:
#         print('try again')
#         continue
#     print('Congratulations!')
#     break
# ______________________________ Задача по циклам
# while True:
#     try:
#         print('the result: ', float(input('enter first num: ')) / float(input('enter second num: ')), '\n')
#     except Exception as e:
#         print(e, "\nTry again, enter two NUMER (second can't be zero)\n")
#         continue
#     flag = input('continue? yes/no: ')
#     if flag in ['yes', 'Yes', 'YES']:
#         print("Let's go :)\n")
#     elif flag in ['no', 'No', 'NO']:
#         print("Bye :(")
#         break
#     else:
#         print("incorrect input, let's try again xD\n")
# ______________________________
# my_set = {2, 10, 20}
# new_set = {val * val for val in my_set}
# print(new_set)
# ______________________________
# my_scores = {
#     'a': 10,
#     'b': 25,
#     'c': 7,
# }
#
# scores = {key: value * 10 for key, value in my_scores.items()}
# print(scores)
# ______________________________
# my_scores = {
#     'a': 'qwer',
#     'b': 'qwertyu',
#     'c': 'qw',
#     'd': 'q',
# }
#
# scores = {key: value.upper() for key, value in my_scores.items()}
# print(scores)
# ______________________________
# my_list = ['qwerty', 'qwer', 'q', 'w', 'qwe', 'qw']
#
# new_list = [elem for elem in my_list if len(elem) > 3]
# print(new_list)
# ______________________________
