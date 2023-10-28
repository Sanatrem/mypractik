# def decorator(func):
#     def tipa_func(a):
#         print('nachalo')
#         func(a)
#         print('konech')
#     return tipa_func
# def header(fun2):
#     def tip2(b):
#         print('<hi>')
#         fun2(b)
#         print('</hi>')
#     return tip2
# @header
# def name(name1):
#     print('hello',name1)

# a = str(input('enter your name: '))
# name(a)

# def a(b):
#     def c(d):
#         print('nachalo')
#         b(d)
#         print('conec')
#     return c
# def a2(b2):
#     def c2(d2):
#         print('model')
#         b2(d2)
#         print('eto vse')
#     return c2
# @a2
# def a3(a4):
#     print('is', a4)

# a3('Ifone 15')
# print(2023)

# def a(a1):
#     def b(*args, **kwargs):
#         print('Name, ysername:')
#         a1(*args, **kwargs)
#         print('Ok')
#     return b
# def s(s1):
#     def d(*args, **kwargs):
#         print('Year:')
#         s1(*args, **kwargs)
#         print('Good')
#     return d
# @a
# def c(c1):
#     print(c1)
# c('Sanat, Ishenbekov')
# @s
# def f(f1):
#     print(f1)
# f(2007)

# def a(a1):
#     def b(*args, **kwargs):
#         print('сколько тебе лет?')
#         a1(*args, **kwargs)
#         print('спасибо')
#     return b
# @a
# def c(c1):
#     print(16)

# a = input(':')
# c(a)

# def j(j1):
#     def k(*args, **kwargs):
#         print('Ваше имя, отчество и год рождения.')
#         j1(*args, **kwargs)
#         print('на этом все.')
#     return k
# a = input('Введите ваше имя: ')
# b = input('фамилия: ')
# c = input('год рождения: ')
# @j
# def n(n1):
#     print(n1)
# n(a + ' ' + b + ' ' + ' ' + c)
