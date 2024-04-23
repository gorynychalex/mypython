# Арифметические выражения

print ( "Введите числа: " )
a = float ( input("a = ") )
b = float ( input("b = ") )

m = a * b
print("Умножение: a * b = " + str(a) + " * " + str(b) + " = " 
      + str(m))

d = a / b
print("Деление: a / b = " + str(a) + " / " + str(b) + " = " 
      + str(d))

d1 = a // b
print("Целочисленное деление: a // b = " + str(a) + " // " + str(b) + " = " 
      + str(d1))

d2 = a % b
print("Остаток от деления: a % b = " + str(a) + " % " + str(b) + " = " + str(d2))