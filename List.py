# # Тема: Список(list) -- Тизме
# # Список(list) - """Бул ирээтелген жана озгоруучу коллекция деп айтсак болот, мындайча айтканда список ар кандай объекттерди озуго камтышы мумкун (анын ичинде ички тизмелер да кирет) же эч нерсе сакталбашы мумкун.
# # Python тилинде список торт бурчтук каша менен жазылат![]"""

# # 'Пустой список жаратуу жолдору:'

# # '1) Переменнный аркылуу:'
# # list = [' 2 3 4 5 6']
# # print(list)

# # thislist = ["apple", "banana", "cherry"]
# # print(thislist)

# # mylist = ["apple", "banana", "cherry"]
# # print(type(mylist))

# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


#1 сандарды ирети менен чыгаргыла
# list = [1,2,3,4,5,7,8,56,45,23]
# thislist = [1,2,3,4,5,7,8,56,45,23]
# thislist.sort()
# print(thislist)

# #2 бул списоктун узундугун тапкыла
# list = [1,2,3,4,5,7,8,'Title', ' одирнарный']
# print(len(list))

# #3 бул жактан int,float, алып салгыла
# list = [True, 90.3, False, 'str', 123, 90j]
# thislist = [True, 90.3, False, 'str', 123, 90j]
# thislist.pop(1)
# thislist.pop(3)
# print(thislist)

# #4 бул жака дагы бир элемент кошкула
# list = ['asta', 'levi', 'isagi','luffy','zoro']
# thislist = ['asta', 'levi', 'isagi','luffy','zoro']
# thislist.append('Nami')
# print(thislist)

# #5 баардык элементтерди алып салгыла
# list = [True, 90.3, False, 'str', (123,), 90j]
# thislist = [True, 90.3, False, 'str', (123,), 90j]
# thislist.clear()
# print(thislist)

# list = [True, 90.3, False, 'str', (123,), 90j]
# list.clear()
# print (list)
