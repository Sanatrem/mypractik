# #1
# mylist = ['Luffi', 'Nami', 'Zoro', 'Usop']
# print(mylist)

# #2
# a = ['Luffi', 'Nami', 'Zoro', 'Usop']
# a.append('Sangi')
# print(a)

# #3
# a = ['Luffi', 'Nami', 'Zoro', 'Usop']
# a.insert(0, "3")
# print(a)

# #4
# a = ['Luffi', 'Nami', 'Zoro', 'Usop']
# int =  ("3")
# a.extend(int)
# print(a)

# #5
# a = ['Luffi', 'Nami', 'Zoro', 'Usop']
# mytuple = ("Bruk",)
# a.insert(0, mytuple)    
# print(a)

# #6
# a = ['Luffi', 'Nami', 'Zoro', 'Usop']
# a.insert(1, 'FRenke')
# print(a)

# #7
# a = ['Luffi', 'Nami', 'Zoro', 'Usop']
# a.remove('Bon')
# print(a)

# #8
# a = ['Luffi', 'Nami', 'Zoro', 'Usop']
# print(len(a))

# 1
# x = {"apple", "banana", "cherry"}

# 2
# x = {"apple", "banana", "cherry"}
# x.remove("apple")
# print(x)

# 3
# x = {"apple", "banana", "cherry"}
# x.add("stravberi")
# print(x)

# 4
# x = {"apple", "banana", "cherry"}
# xx = {'Luffi', 'Zoro', 'Sangi'}
# x.update(xx)
# print(x)

# 5 
# x = {"apple", "banana", "cherry"}
# print(len(x))

# 1. 
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.

# 2
# Выведите первый и последний элемент списка.
# lst = [1, 2, 3, 4, 5]

# 3.
# Строки в python обозначаются кавычками. Приведите все способы.

# 4.
# Как проверить наличие элемента в списке?

# a = [1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
# print(a[0:4])

# lst = [1, 2, 3, 4, 5]
# lst.pop(1)
# lst.pop(2)
# lst.remove(3)
# print(lst)

# ''
# ""
# """"""

# a = [1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
# if 89 in a:
#     print('yes')

# ysername = 'sanat'
# password = 5545
# num = str(input('Ведите имя!'))
# num = int(input('Ведите пароль! '))

# if num == ysername:
#     if num == password: 
#         print('Доступ открыт')
# else:
#     print('Доступ закрыт')


# прочитать про def

# password = 5545
# num = int(input('Ведите пароль!:'))
# if num == password:
#     print('Доступ открыт')
# else:
#     print('Доступ закрыт попроюуйте еще раз:')
#     while True:
#         b = int(input('Ведите пароль!:'))
#         if b == password:
#             print('Доступ открыт')
#         else:
#             print('Доступ закрыт попроюуйте еще раз:')

# ysername = 'sanat'
# password = 5545
# num = str(input('Ведите имя!'))
# nut = int(input('Ведите пароль! '))
# def a():
#     if num == ysername:
#         if nut == password: 
#             print('Доступ открыт')
#     else:
#         print('Доступ закрыт')
#         while True:
#             b = str(input('Ведите имя!'))
#             v = int(input('Ведите пароль! '))
#     if b == ysername:
#          if v == password: 
#              print('Доступ открыт')
#     else:
#         print('Доступ закрыт')
# a()

# 1 Создайте копию списка my_list и выведите её
# my_list = [1, 2, 3, 4, 5]

# 2 Отсортируйте список в порядке убывания и выведите его.
# my_list = [5, 2, 8, 1, 3]

# 3 Удалите элемент с индексом 2 из списка и выведите список после удаления.
# my_list = [1, 2, 3, 4, 5]

# 4 Добавьте элемент в конец списка и затем удалите элемент из начала списка.
# fruits = ['яблоко', 'груша', 'апельсин']

# 5 Найдите максимальное и минимальное значения в списке чисел.
# numbers = [15, 30, 10, 45, 20]

# 6 Удалите повторяющиеся элементы из списка.
# numbers = [1, 2, 2, 3, 4, 4, 5]

# my_list = [1, 2, 3, 4, 5]
# print(my_list)

# my_list = [5, 2, 8, 1, 3]
# print(sorted(my_list))

# my_list = [1, 2, 3, 4, 5]
# my_list.pop(2)
# print(my_list)

# fruits = ['яблоко', 'груша', 'апельсин']
# fruits.append('слива')
# fruits.pop(0)
# print(fruits)

# numbers = [15, 30, 10, 45, 20]
# print(numbers[2:4])

# numbers = [1, 2, 2, 3, 4, 4, 5]
# numbers.pop(2)
# numbers.pop(4)
# print(numbers)

# 1 Создайте множество numbers, содержащее числа от 1 до 10. Напишите код, который удаляет все четные числа из множества.
# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 2 Создайте множество fruits, содержащее несколько названий фруктов. Затем добавьте новый фрукт в множество и удалите один из существующих фруктов.
# fruits = {"яблоко", "груша", "апельсин", "банан"}

# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# def even(a):
#     if a%2==0:
#         del(a)
#     else:
#         print(a,'не четное')
# for i in numbers:
#     even(i)

# fruits = {"яблоко", "груша", "апельсин", "банан"}
# fruits.add('слива')
# fruits.remove('яблоко')
# print(fruits)

# i = 1
# while i < 101:
#   print (i)
#   if i ==52:
#     break
#   i += 1
    
# 1 Объединить строки:
# str1 = 'Hello'
# str2 = 'World'

# 2 Напишите программу, которая принимает строку от пользователя и выводит эту строку в обратном порядке.

# 3 Преобразовать строку в верхний или нижний регистр:
# str = "Hello World"

# 3 Напишите программу, которая принимает строку от пользователя и подсчитывает количество символов в этой строке   

# str1 = 'Hello'
# str2 = 'World'
# c = str1 + str2
# print(c)

# a = 'sanat'
# print(a[::1])

# a = input()[::-1]
# print(a)

# str = "Hello World"
# print(str.upper())

# a = input()
# print(len(a)) 

# def s():
#     a = int(input('ff'))
#     b = int(input('cc'))
#     c = a + b
#     print(c)
# s()

# гит, гитхаб

# 1 функция менен эки аргумеnти кошкула
# def sum(a, b):

#  2 бир аргумент берип жуп санбы же так санбы чыгарып бергиле
#  def sum(число):

# def sum(a, b):
#     print(a + b)
# sum(23,34)

# def sum():
#     if a %2==0:
#         print('четное')
#     else:
#         print('ne chetnoe')
# sum()

# a = 100
# b = 200
# a,b=b,a
# print(a)
# print(b)

# import random
# def red():
#     s = ['frenki', 'zoro', 'luffi']
#     random.choice(s)
# def game():
#     lan = red()
#     str = len(lan)
#     popytki = 0
#     rai = 5
#     abc = ['_'] * str

#     print('shbhjdnbcjn')
#     print('sdjfbjhdnv', rai, )

# import random

# def угадай_слово(слова, макс_попыток):
#     # Выбираем случайное слово из списка
#     загаданное_слово = random.choice(слова)
    
#     # Преобразуем загаданное слово в список букв
#     буквы_слова = list(загаданное_слово)
    
#     # Создаем список, чтобы хранить отгаданные буквы
#     отгаданные_буквы = ['_'] * len(буквы_слова)
    
#     # Переменная для хранения текущего количества попыток
#     попытки = 0
    
#     # Сообщаем пользователю, сколько букв в слове
#     print(f"Угадайте слово, состоящее из {len(буквы_слова)} букв.")
    
#     # Начинаем игровой цикл
#     while попытки < макс_попыток:
#         # Выводим текущее состояние отгаданных букв
#         print(' '.join(отгаданные_буквы))
        
#         # Запрашиваем у пользователя букву
#         буква = input("Введите букву: ").lower()
        
#         # Проверяем, что введена ровно одна буква
#         if len(буква) != 1:
#             print("Пожалуйста, введите только одну букву.")
#             continue
        
#         # Проверяем, что введена буква, а не что-то другое
#         if not буква.isalpha():
#             print("Пожалуйста, введите букву, а не цифру или символ.")
#             continue
        
#         # Проверяем, была ли буква уже отгадана
#         if буква in отгаданные_буквы:
#             print("Эта буква уже была отгадана.")
#             continue
        
#         # Проверяем, есть ли введенная буква в загаданном слове
#         if буква in буквы_слова:
#             # Обновляем список отгаданных букв
#             for i in range(len(буквы_слова)):
#                 if буквы_слова[i] == буква:
#                     отгаданные_буквы[i] = буква
#             # Проверяем, все ли буквы отгаданы
#             if '_' not in отгаданные_буквы:
#                 print("Поздравляем! Вы угадали слово:", загаданное_слово)
#                 break
#         else:
#             print("Эта буква не входит в слово.")
        
#         попытки += 1
    
#     # Если закончились попытки и слово не угадано
#     if '_' in отгаданные_буквы:
#         print("Игра окончена. Загаданное слово было:", загаданное_слово)

# # Пример использования функции
# список_слов = ["яблоко", "банан", "апельсин", "груша", "вишня"]
# максимальное_количество_попыток = 12
# угадай_слово(список_слов, максимальное_количество_попыток)

# a = int(input('ведите час от 1 до 23 :'))
# if a < 11:
#     print('доброе утро')
# elif a < 17:
#     print('добрый день')
# elif a > 17:
#     print('добрый вечер')

# a = int(input('ведите дни недели от 1 до 7:'))
# if a == 1:
#     print('понедельник')
# elif a == 2:
#     print('вторник')
# elif a == 3:
#     print('среда')
# elif a == 4:
#     print('четверг')
# elif a == 5:
#     print('пятница')
# elif a == 6:
#     print('субота')
# elif a == 7:
#     print('воскресене')


# # Запрос ввода количества баллов от пользователя
# try:
#     received_points = float(input("Введите количество полученных баллов: "))
# except ValueError:
#     print("Пожалуйста, введите число.")
#     exit()

# # Определение уровня на основе количества баллов
# if received_points >= 90:
#     level = "Отлично"
# elif received_points >= 70:
#     level = "Хорошо"
# elif received_points >= 50:
#     level = "Удовлетворительно"
# else:
#     level = "Неудовлетворительно"

# # Вывод результата
# print(f"Ваш уровень: {level}")

# a = int(input('ведите число:'))
# if a < 0:
#     print('отрицательный')
# elif a > 0:
#     print('положительный')

# a = ['str']
# b = 'apple'
# c = {'str', True}
# a,b,c=b,a,c
# print(a)

# for i in range(1,31,2):
#     print(i)

# list = [1, 2, 3, 4]
# a = int(input('ведите число:'))
# if a in list:
#     print('gg')
# else:
#     print('hh')

# a = input('ведите первое число:')
# b = input('ведите второе число:')
# if a > b:
#     print(b, 'menshe', a)
# elif a < b:
#     print(b, 'bolshe', a)
# elif b > a:
#     print(b, 'menshe', a)
# elif b > a:
#     print(b, 'bolshe', a)

# a = input("Пожалуйста, введите что-то: ")
# try:
#     a = float(a)
#     if a.is_integer():
#         b = "class int"
#     else:
#         b = "class float"
# except ValueError:
#     b = "class str"
# print(f"Введенные вами данные являются: {b}")

# def a():
#     a = int(input('number:'))
#     if a%2==0:
#         print(a,'четное')
#     else:
#         print(a,'не четное')
# a()

def a(b):
    return lambda a : a * b
    
s = a(5)
print(s(6))
x = lambda a, b : a + b
print(x(5, 6))
x = lambda a, b : a - b
print(x(5, 6))
