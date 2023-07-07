#  Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.


def power(a , b):       
    if b == 0:
        return 1

    elif b < 1:
        b *= -1
        return 1 / (power(a, b - 1) * a)

    elif b == 1:
        return a

    else:
        return power(a, b - 1) * a


a = 2  # int(input("Enter the first number: "))
b = -8  # int(input("Enter the second number: "))



print(f"{a} ^ {b} = {power(a, b)} ")

print(f"{a} ^ {b} = {pow(a, b)} ")  




# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


a = 66  # int(input("Enter the first number: "))
b = 82  # int(input("Enter the second number: "))


def sum(a, b):
    try:
        if a < 0 or b < 0:
            raise ValueError("Both arguments must be non-negative")
        elif a == 0 and b > 0:
            return b
        else:
            return sum(a - 1, b + 1)
    except ValueError as e:
        print(e)


print(f"{a} + {b} = {sum(a, b)} ")

print(f"{a} + {b} = {a + b} ")