#Напишите выражение (задание на самопроверку).
#Дано n-значное целое число N. Определите, входят ли в него цифры 3 и 7.
Number = list(str(input("Print any number: ")))
print(Number)
Search = list(map(int, Number))
print(Search)
print(3 in Search and 5 in Search)

