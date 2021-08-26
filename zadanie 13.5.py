#Запишите условие, которое является истинным,
# когда только одно из чисел А, В и С меньше 45.
# Иногда проще записать все условия и не пытаться упростить их.

a = int(input("Print a: "))
b = int(input("Print b: "))
c = int(input("Print c: "))

if ((a < 45) and (b >= 45) and (c >= 45)):
    print("one number a<45 ", a)
elif ((a >= 45) and (b < 45) and (c >= 45)):
    print("one number b<45 ", b)
elif ((a >= 45) and (b >= 45) and (c < 45)):
    print("one number c<45 ", c)
else:
    print("All numbers >45 or =45")

A = int(input('Введите первое число\n'))
B = int(input('Введите второе число\n'))
C = int(input('Введите третье число\n'))

if ((A < 45) and (B >= 45) and (C >=45)) or \
    ((A >= 45) and (B < 45) and (C >=45)) or \
    ((A >= 45) and (B >= 45) and (C < 45)):
    print('Есть число меньше 45 и только одно')
else:
    print('Числа меньше 45 нет или их несколько')