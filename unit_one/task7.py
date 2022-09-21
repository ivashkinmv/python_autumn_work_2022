# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

a_point = float(input("Введите координату X точки А: "))
b_point = float(input("Введите координату X точки B: "))
c_point = float(input("Введите координату X точки C: "))

print(abs(c_point - a_point))
print(abs(b_point - c_point))
print(abs(c_point - a_point) + abs(b_point - c_point))
