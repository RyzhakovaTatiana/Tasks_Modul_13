#Задание на самопроверку.

#Создайте скрипт, который будет в input() принимать строки,
# их необходимо будет конвертировать в числа,
# добавьте try-except, чтобы строки могли быть сконвертированы в числа.
#В случае удачного выполнения скрипта пусть выведется: «Вы ввели правильное число».
#В конце скрипта обязательно должна быть надпись «Выход из программы».

try:
    print("Need any string!")
    stroka = int(input("Print any string: "))
    print("You printed varyable number: ", stroka)
except ValueError:
    print("You didn't enter numbers! Please, enter numbers!")
finally:
    print("Exit! Good job!")





