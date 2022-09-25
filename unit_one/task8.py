# todo: Даны переменные A, B, C. Написать код который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:
A = 1
B = 2
C = 3
# Итоговый результат должен быть:
# A = 3
# B = 7
# C = 10

# Пример 2:
# A = 2
# B = 10
# C = 7
# Итоговый результат должен быть:
# A = 2
# B = 7
# C = 10

# a_var
# b_var
# c_var

# A = float(input("Введите значение А: "))
# B = float(input("Введите значение B: "))
# C = float(input("Введите значение C: "))

# TODO: Решение 1.

if (A < B > C) and A > C:
    print("A =", C)
    print("B =", A)
    print("C =", B)
elif (A < B > C) and A < C or (A == C < B):
    print("A =", A)
    print("B =", C)
    print("C =", B)
elif (A > B < C) or (B == C < A):
    print("A =", B)
    print("B =", C)
    print("C =", A)
else:
    print("A =", A)
    print("B =", B)
    print("C =", C)

# TODO: Решение 2.
lst = sorted([A, B, C])
print("A =", lst[0])
print("B =", lst[1])
print("C =", lst[2])
