#Проверьте, все ли элементы в списке являются уникальными.
L = input("Print a list: ")
unicum = list(set(L))
if len(unicum) < len(L):
    print("Ne vse elementi unikalnie")
else:
    print("Vse elementi unikalnie")

#Дано натуральное восьмизначное число. Выясните,
# является ли оно палиндромом (читается одинаково слева направо и справа налево).
pal = str(input("Enter 8 numbers:\n "))
if pal == pal[::-1]:
    print("Palindrom!")
else:
    print("Ne palindrom")
