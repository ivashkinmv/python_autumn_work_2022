# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

a_point = float(input("Введите координату X точки А: "))


if a_point == 0:
    a_point = float(input("Введите координату X точки А, отличную от 0: "))
    b_point = float(input("Введите координату X точки B: "))
    x = -(b_point / a_point)
    print(x)
else:
    b_point = float(input("Введите координату X точки B: "))
    x = -(b_point / a_point)
    print(x)
