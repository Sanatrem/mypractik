# import turtle

# # Создаем объект Turtle
# pen = turtle.Turtle()

# # Устанавливаем скорость рисования
# pen.speed(0)  # Максимальная скорость

# # Определяем функцию для рисования квадрата
# def нарисовать_квадрат():
#     for _ in range(4):
#         pen.forward(50)  # Длина стороны квадрата
#         pen.right(90)    # Поворот на 90 градусов

# # Вложенные циклы для создания узора из 100 квадратов
# for _ in range(10):  # Внешний цикл для 10 строк
#     for _ in range(10):  # Внутренний цикл для 10 квадратов в строке
#         нарисовать_квадрат()
#         pen.penup()  # Поднимаем перо, чтобы переместиться к следующему квадрату
#         pen.forward(60)  # Расстояние между квадратами в строке
#         pen.pendown()  # Опускаем перо, чтобы начать рисовать следующий квадрат
    
#     # Перемещаемся к началу следующей строки
#     pen.penup()
#     pen.goto(0, pen.ycor() - 60)  # Расстояние между строками
#     pen.pendown()

# # Завершение работы
# turtle.done()

# import random

# def get_user_choice():
#     """Запрашивает выбор пользователя (камень, ножницы или бумагу)."""
#     while True:
#         user_choice = input("Выберите: камень, ножницы или бумага? ").lower()
#         if user_choice in ["камень", "ножницы", "бумага"]:
#             return user_choice
#         else:
#             print("Пожалуйста, введите камень, ножницы или бумагу.")

# def get_computer_choice():
#     """Случайный выбор компьютера (камень, ножницы или бумага)."""
#     choices = ["камень", "ножницы", "бумага"]
#     return random.choice(choices)

# def determine_winner(user_choice, computer_choice):
#     """Определяет победителя и возвращает результат раунда."""
#     if user_choice == computer_choice:
#         return "Ничья!"
#     elif (user_choice == "камень" and computer_choice == "ножницы") or \
#          (user_choice == "ножницы" and computer_choice == "бумага") or \
#          (user_choice == "бумага" and computer_choice == "камень"):
#         return "Вы победили!"
#     else:
#         return "Компьютер победил!"

# def play_game():
#     """Главная функция игры."""
#     print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
#     while True:
#         user_choice = get_user_choice()
#         computer_choice = get_computer_choice()
        
#         print(f"Ваш выбор: {user_choice}")
#         print(f"Выбор компьютера: {computer_choice}")
        
#         result = determine_winner(user_choice, computer_choice)
#         print(result)
        
#         play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
#         if play_again != "да":
#             break

# if __name__ == "__main__":
#     play_game()

# import random

# # Список слов для угадывания
# words = ["яблоко", "банан", "груша", "апельсин", "вишня", "арбуз"]

# def choose_word():
#     """Выбирает случайное слово из списка."""
#     return random.choice(words)

# def display_word(word, guessed_letters):
#     """Отображает текущее состояние угадываемого слова."""
#     display = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display += letter
#         else:
#             display += "_"
#     return display

# def play_game():
#     """Главная функция игры."""
#     print("Добро пожаловать в игру 'Угадай слово'!")
#     word_to_guess = choose_word()
#     guessed_letters = []
#     attempts = 6  # Количество попыток
    
#     print(f"У вас есть {attempts} попыток, чтобы угадать слово.")
    
#     while attempts > 0:
#         print("\n" + display_word(word_to_guess, guessed_letters))
        
#         guess = input("Угадайте букву или слово целиком: ").lower()
        
#         if guess == word_to_guess:
#             print(f"Поздравляю! Вы угадали слово: {word_to_guess}")
#             break
        
#         if len(guess) == 1 and guess.isalpha():
#             if guess in guessed_letters:
#                 print("Вы уже угадали эту букву.")
#             elif guess in word_to_guess:
#                 guessed_letters.append(guess)
#                 print("Правильно!")
#             else:
#                 attempts -= 1
#                 print(f"Неправильно! У вас осталось {attempts} попыток.")
#         else:
#             print("Пожалуйста, введите одну букву или попробуйте угадать слово целиком.")

#     if attempts == 0:
#         print(f"Извините, вы проиграли. Загаданное слово было: {word_to_guess}")

# if __name__ == "__main__":
#     play_game()
