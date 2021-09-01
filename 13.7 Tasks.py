some_var = (2,)
if some_var is None:
    print("NoneType")
else:
    print(type(some_var))

#На вход нашей программы подается число. А мы хотим проверить, является ли оно целым,
# находится ли в определенном промежутке (например от 100 до 999 включительно),
# да еще и делится ли на 2 и 3 одновременно.
a = int(input("Print number: "))
if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print("OK")
else:
    print("Mistake")

#Напишите программу, которая на вход принимает последовательность целых чисел
# и возвращает True, если все числа равны нулю,
# и False, если найдется хотя бы одно ненулевое число.
# Разрешается использование только логических операторов и функций all([ ]) и any([ ]).
num = str(input("Vvedite posledovatelnost: "))
N = list(map(int, num.split()))
print(N)
print(not any(N))

#Программа должна выводить True, если есть хотя бы одно четное число.
L = [int(input("vvedite chislo: ")) % 2 == 0 for i in range(5)]
print( any(L))

