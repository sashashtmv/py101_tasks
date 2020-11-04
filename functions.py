"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное

def get_number(n):
    for char in n:
        if int(char) and (int(char) % 2 == 0):
            print(f"Число: {int(char)} - четное.")

get_number(input("Напишите любые числа, чтобы узнать, какое из них четное ").split())

# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
def sell_alcohol():
    pass

age = 17
sell_alcohol if age > 21 else print('Мы не продаём алкоголь несовершеннолетним.')


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
import keyword

def check_words(str):
    if keyword.iskeyword(str):
        print(f"Строка - {str} является ключевым словом в Python")

check_words(input("Проверь свое слово - "))

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."

def get_type(arg):
    if type(arg) is str:
        print("Это строка")
    elif type(arg) is int:
        print("Это число")
    elif type(arg) is bool:
        print("Это булевый")
    elif type(arg) is tuple:
        print("Это кортеж")
    elif type(arg) is set:
        print("Это множество")
    elif type(arg) is dict:
        print("Это словарь")
    else:
        print("Это none")
    print(type(arg))

get_type(1)
get_type("hello")
get_type(True)
get_type((1, 2, 3))
get_type({1, 2, 3, 4, 5, 6})
get_type({'dict': 1, 'dictionary': 2})
get_type(None)