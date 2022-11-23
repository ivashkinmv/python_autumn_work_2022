# todo: Реализовать собственный класс исключений, которые будут вызываться (бросаться) в случае:
#  1. пользователь ввел некорректное значение в заданном диапазоне
#  2. результат запроса вернул 0 строк
#  3. Произошел разрыв соединения с сервером


class IndexIsOutOfRange(IndexError):
    def __init__(self):
        super().__init__(f"Тра-та-та. Исключение сработало")

try:
    ind = int(input("Число для сравнения: "))
    if 3 > ind:
        raise IndexIsOutOfRange()
except IndexIsOutOfRange as e:
    print(e)


import psycopg2
connection = psycopg2.connect(
            host="localhost",
            database="hotel",
            user="postgres",
            password="162657")

cur = connection.cursor()


class CheckStringError(Exception):
    def __init__(self):
        super().__init__(f"Тра-та-та. Ваш запрос не удовлетворяет условиям")


try:
    sql_select = f"""SELECT rooms_name
                from rooms
               where rooms_id = 8"""
    cur.execute(sql_select)

    records = cur.fetchall()
    if not records:
        raise CheckStringError()

except CheckStringError as e:
    print(e)



import psycopg2


class ConnectionIsDown(Exception):
    def __init__(self):
        super().__init__(f"Тра-та-та. Упало соединение")


try:
    conn = psycopg2.connect(
        host="localhost",
        database="hotel",
        user="postgres",
        password="162657")
    raise ConnectionIsDown()
except ConnectionIsDown as e:
    print(e)
