# Условный оператор

print ( "Введите два числа: " )
a = int ( input("a = ") )
b = int ( input("b = ") )

if a > b:
    M = a
else:
    M = b

print(M)

M1 = max(a,b)

print(M1)

M2 = a if a > b else b

print(M2)

if a < 10 and b < 10:
    print("a и b - одноразрядные числа")
elif a >= 10 and b >= 10 and a < 100 and b < 100:
    print("a и b - числа в диапазоне от 10 до 99")
else:
    print("разные числа")