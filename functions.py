# Функции
# print(__name__)

CONSTANS="Файл с функциями"

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y


def newfunc(n):
    def myfunc(x):
        return n+x
    return myfunc

# Аргументы
def func(a,b,c=2):
    return a + b + c


# Переменное количество аргументов
def funcVarargs(*args):
    return args

def sumDigits(n: int|float) -> int|float:
    sum = 0
    while n!= 0:
        sum += n % 10
        n = n // 10
    return sum

# Рекурсивные функции
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def recursive_sum(arr):
    if not arr:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])

def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial_tail(n-1, n*acc)

# args - кортеж

# funcVarargs(1,2,3,'aaaa','bbb')

# Функция может принимать произвольное число именованных аргументов 
# перед именем ставится **
def funcKWargs(**kwargs):
    return kwargs

if __name__ == "__main__":

    a = add(10,15)
    print(a)

    # new = newfunc(100)
    # print(new)
    # print(new(200))
    # print(func(1,2))
    # print(func(1,2,3))
    # print(funcKWargs(a=1,b=2,c=3))

    # print(factorial(5))
    # print(factorial_tail(5))
    # print(fibonacci(10))
    # print(recursive_sum([10,20,30]))
    