# todo: Реализовать собственный класс исключений, которые будут вызываться (бросаться) в случае:
#  1. пользователь ввел некорректное значение в заданном диапазоне
#  2. результат запроса вернул 0 строк
#  3. Произошел разрыв соединения с сервером

from random import randint

dig = randint(9,10)
ind = randint(9,10)
l1 = [i + 1 for i in range(1, dig + 1)]
print(l1)

# class IndexIsOutOfRange(Exception):
#     def __init__(self, number):
#         super().__init__(f"Тра-та-та")
#
# try:
#     if len(l1) < ind:
#         raise IndexIsOutOfRange(ind)
# except IndexIsOutOfRange(ind) as e:
#     print(e)

# class IndexIsOutOfRange(IndexError):
#     pass
# # def verify(digit):
# #     if len(digit) < 2:
# #         raise IndexIsOutOfRange("dmamdam")
#
# try:
#     verify = int(input('Число: '))
#     if verify < 2:
#         raise IndexIsOutOfRange("dmamdam")
#     print(verify + 2.1)
# except IndexIsOutOfRange as e:
#     print(e)
#
# class NegValException(Exception):
#     pass
# # def verify(digit):
# #     if len(digit) < 2:
# #         raise IndexIsOutOfRange("dmamdam")
#
# try:
#     verify = int(input('Число: '))
#     if verify < 0:
#         raise NegValException("Neg val: " + str(verify))
#     print(verify + 10)
# except NegValException as e:
#     print(e)


# def validate(name):
#     if len(name) < 6:
#         raise ValueError
#     else:
#         print("Принято")
# try:
#     name = input("Введите имя:")
#     validate(name)
# except ValueError:
#     print("Имя слишком короткое:")

class NegValException(Exception):
    def __init__(self, number):
        super().__init__(f"Neg val: {number}")
        self.number = number
try:
    val = int(input("input positive number: "))
    if val < 0:
        raise NegValException(val)
except NegValException as e:
    print(e)


