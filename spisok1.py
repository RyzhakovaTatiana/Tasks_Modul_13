

sp1 = list(str(123456789))
print(list(map(int, sp1)))
list_digit = list(map(int, sp1))
print(list_digit)
print(5 in list_digit)

#Запишите логическое выражение, которое определяет,
# что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.

A = int(input("Print A: "))
if not (-10 <= A <= -1 or 2 <= A <= 15):
    print("Числа А нет в этом интервале")
else:
    print("Число тут")

#Дано двузначное число. Определите, входит ли в него цифра 5.
# Попробуйте решить задачу с использованием целочисленного деления и деления с остатком.
N = int(input("Print N: "))
if (N // 10 != 5 and N % 10 != 5):
    print("Chisla 5 net")
else:
    print("Chislo 5 est")
    