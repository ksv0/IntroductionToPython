# ������ 26:  �������� ���������, ������� �� ���� ��������� ��� ����� A � B, � �������� ����� � � ����� ������� B � ������� ��������.


def power(a, b):
    try:
        if b < 0:
            raise Exception(
                "if we could raise to a negative power but we can't, enter a non-negative power and divide one by the result"
            )

        if b == 0:
            return 1

        elif b == 1:
            return a

        else:
            return power(a, b - 1) * a
    except Exception as e:
        print(e)


# def power1(a , b, c=0):       # � �������������� �� �������� # ����� 4 ���� � ����� �����
#    print(f"a = {a} b = {b} c = {c} ")
#    if b<0:

#        c =+ 1
#        b = b * (-1)
#    print(f"a = {a} b = {b} c = {c} ")

#    if b == 0:
#        return 1

#    elif b == 1 & c == 1:
#        return 1 / a

#    elif b == 1:
#        return a

#    else:
#        return power(a, b - 1, c) * a


a = 2  # int(input("Enter the first number: "))
b = -8  # int(input("Enter the second number: "))


print(f"{a} ^ {b} = {power(a, b)} ")


print(f"{a} ^ {b} = {pow(a, b)} ")  # ���� # ���� �� ������������� ���� ����


# ������ 28: �������� ����������� ������� sum(a, b), ������������ ����� ���� ����� ��������������� �����. �� ���� �������������� �������� ����������� ������ +1 � -1. ����� ������ ������������ �����.


a = 66  # int(input("Enter the first number: "))
b = 82  # int(input("Enter the second number: "))


def sum(a, b):
    try:
        if a < 0 or b < 0:
            raise ValueError("Both arguments must be non-negative")
        elif a == 0 and b > 0:
            return b
        elif b == 0 and a > 0:
            return a
        else:
            return sum(a - 1, b + 1)
    except ValueError as e:
        print(e)


print(f"{a} + {b} = {sum(a, b)} ")
