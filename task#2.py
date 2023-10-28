# a = [1, 2, 3, 4, 5]
# b = iter(a)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# while True:
#     a = 'sanat'
#     p = '1234'
#     d = input('login:')
#     c = input('password:')
#     if a in ('sanat', 1234):
#         print('try')
#     else:
#         print('error')

# import calendar
# print(calendar.calendar(2050))

# a = int(input("ведите оценку: "))
# if a in (2, 3):
    # print("не прошли.")
# elif a in (4, 5):
    # print("прошли.")
# else:
    # print("ведена неправильная оценка.")

# for i in range(1, 10):
    # print(str(i) * i)

# a = 'as, dsf, d'
# print(a.upper())
# print(a.isupper())
# print(a.lower())
# print(a.islower())
# print(a.capitalize())
# print(a.find('s'))
# print(a.split(','))
# b = a.split(', ')
# print(b[1])
# for i in range(len(b)):
#     b[i] = b[i].capitalize()
# print(b)

# num = [1, 2, 3, 4, 5, 6, 7]
# num.pop()
# num.pop(4)
# num.remove(1)
# num.clear()
# print(num.count(4))
# print(len(num))
# num = [1, 2, 3, 4, 5, 6, 7]
# num.reverse()
# print(num)
# num = [1, 2, 3, 4, 5, 6, 7]
# num.sort()
# print(num)

# fruits = ["яблоко", "банан", "апельсин"]
# for fruit in fruits:
#     print(fruit)

# for i in range(1, 101):
#     if i%2==0:
#         print(i)

# i = 1
# while i <=100:
#     # if i%2==0:
#     print(i)
#     i += 1
#     if i%2==0:
#         print(i)

# def inf(all):
#     def inf2(all2):
#         print('year')
#         all2(all)
#         print('name')
#     return inf2
# @inf
# def year(inf3):
#     print('is', inf3)
# year(16) 
# print('sanat')

# a = input('kakaya komanda: ')
# b = 2008
# print(a + "chempion" + str(b))

# a = int(input('введите число: '))
# print(a **3)

# a = 15
# print('для числа 15 предыдущее', a -1)
# print('для числа 14 предыдущее', a -2)
# print('для числа 13 предыдущее', a -3)
# print('для числа 12 предыдущее', a -4)
# print('для числа 11 предыдущее', a -5)
# print('для числа 10 предыдущее', a -6)
# print('для числа 9 предыдущее', a -7)
# print('для числа 8 предыдущее', a -8)
# print('для числа 7 предыдущее', a -9)
# print('для числа 6 предыдущее', a -10)
# print('для числа 5 предыдущее', a -11)
# print('для числа 4 предыдущее', a -12)

# a = int(input('number: '))
# b = int(input('nimber2: '))
# print(f'{a} + {b} =', a + b)
# print(f'{a} - {b} =', a - b)
# print(f'{a} * {b} =', a * b)
# print(str(a) + ' + ' + str(b) + ' = ' + str( a + b ))
# print(str(a) + ' - ' + str(b) + ' = ' + str( a - b ))
# print(str(a) + ' * ' + str(b) + ' = ' + str( a * b ))
# print(str(a) + '---' + str(a *2) + '---' + str(a *3) + '---' + str(a *4) + '---' + str(a *5) + '---' + str(a *6) + '---' + str(a *7) + '---' + str(a *8) + '---' + str(a *9))

# a = int(input('minut: '))
# if a%2==0:
    # print(a /2)
# else:
    # b=a+1
    # print((a+1)//2)

# if a >60:
#     b = a % 60
#     c = a // 60
#     print(str(a) + ' eto ' + str(c) + ' saat ' + str(b) + ' minuta ')
# elif a <60:
#     print(f'0 saat {a} minuta') 

# a = int(input('введите цифру:'))
# if a%2==0:
#     print('четное')
# else:
#     print('не четное')

# a = input('name:')
# b = len(a)
# print(f'данная слово имеет {b} символов')

# a = input('name:')
# for i in range(1, 11):
    # print(str(i) + str(a))

# a = int(input('number: '))
# b = int(input('number2: '))
# for i in range(a, b +1):
#     print(i)

# a = int(input('number: '))
# b = int(input('number2:'))
# if a < b:
#     for i in range(a, b +1):
#         print(i)
# else:
#     for i in range(a, b -1,-1):
#         print(i)

# a = int(input('number: '))
# b = int(input('number2:'))
# if a > b:
#     for i in range(a, b, -2):
#         print(i)

# a = int(input('number: '))
# b = int(input('number2:'))
# for i in range(a, b +1):
#     if i%10==9 or i%17==0 or i%3==0 and i%5==0:
#         print(i)

# a = int(input('number: '))
# b = int(input('number2:'))
# for i in range(1,11):
    # print(f'{a} * {i}  = ', a * i)

# def a(n):
#     b = int(input('number: '))
#     for i in range(b+1):
#         b += 1
#     return b
# for i in range(1, 11):
#     print(i, '!=',a(i), sep=' ')

# Функция для вычисления факториала числа
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# try:
#     num = int(input("Введите  число: "))

#     if num < 0:
#         print("Введите целое число.")
#     else:
#         result = factorial(num)
#         print(f"Факториал числа {num} равен {result}")
# except ValueError:
#     print("Пожалуйста, введите целое число.")

# num = int(input("Введите число: "))
# factorial = 1
# for i in range(1, num +1):
#     factorial *= i
#     print(f"{num}! = {factorial}")

# b = int(input('number: '))
# def a(b):
#     # for i in range(1, 101):
#         if b%3==0:
#             print(True)
#         else:
#               print(False)
# a(b)

# a = int(input('number 1: '))
# b = int(input('number 2: '))
# if a > b:
#     print(f'{a} biggest {b}')
# else:
#     print(f'{a} less {b}')

# a = int(input('number 1: '))
# b = int(input('number 2: '))
# if a > b:
#     print(a)
# else:
#     print(b)

