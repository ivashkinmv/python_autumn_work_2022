import sys

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="hotel",
    user="postgres",
    password="162657")

cur = conn.cursor()

sql_list_rooms = f"""SELECT rooms_name, capacity, q_rooms, tv, fridge, add_service, price 
FROM rooms WHERE status = 'Availible'; """

def menu():
    global cur
    print('Выберете ваше действие: \n'
          ' 1) Посмотреть доступные номера \n'
          ' 2) Фильтр номеров \n'
          ' 3) Забронировать номер \n'
          ' 4) Список постоянных клиентов \n'
          ' 5) Показать информацию по номеру \n'
          ' 6) Выйти из программы')
    input_num = int(input())
    match input_num:
        case 1:

            cur.execute(sql_list_rooms)
            records = cur.fetchall()
            for row in records:
                # print(row)
                print(f'Номер: {row[0]}, Вместимость: {row[1]} человек, Кол-во комнат: {row[2]}, '
                      f'ТВ: {row[3]}, Холодильник: {row[4]}, Доп.сервис: {row[5]}, Цена: {row[6]} ')
            conn.commit()
            # conn.close()
            back = int(input("Назад нажмите: 1"))
            if back == 1:
                menu()
            else:
                sys.exit()
        case 2:
            capacity = int(input("Вместимость: "))
            q_rooms = int(input("Кол-во комнат: "))
            tv = str(input("Наличие ТВ (True/False): "))
            fridge = str(input("Наличие холодильника (True/False): "))
            add_service = str(input("Доп.сервис (True/False): "))
            sql_rooms_choice = f"""SELECT rooms_name, capacity, q_rooms, tv, fridge, add_service, price 
            FROM rooms WHERE status = 'Availible' AND capacity = {capacity} AND q_rooms = {q_rooms} 
            AND TV = {tv} AND fridge = {fridge} AND add_service = {add_service}; """
            cur.execute(sql_rooms_choice)
            records = cur.fetchall()
            # print(cur.fetchall())
            for row in records:
                print(f"Номер: {row[0]}, Цена: {row[6]}")
            conn.commit()

            back = int(input("Назад нажмите: 1"))
            if back == 1:
                menu()
            else:
                sys.exit()
        case 3:
            name = str(input("Введите имя клиента: "))
            status = str(input("Введите статус(Booked/Occupied): "))
            room = int(input("Введите номер комнаты : "))
            sql_name_client = f"""SELECT client_id FROM clients WHERE client_name = '{name}'; """
            cur.execute(sql_name_client)
            record = cur.fetchall()
            for row1 in record:
                sql_update = f"""UPDATE rooms SET client_id = {row1[0]}, status = '{status}' WHERE rooms_name = {room} """
                cur.execute(sql_update)
                conn.commit()
                sql_select_rooms = f"""SELECT rooms_name, capacity, q_rooms, tv, fridge, add_service, price 
    FROM rooms WHERE client_id = {int(row1[0])}; """
                cur.execute(sql_select_rooms)
                # print(cur.execute(sql_update))
                records = cur.fetchall()
            # print(records)
                for row in records:
                    print(f"Номер: {row[0]}, Вместимость: {row[1]}, Кол-во комнат: {row[2]}, "
                          f"ТВ: {row[3]}, Холодильник: {row[4]}, Доп.сервис: {row[5]}, Цена: {row[6]} ")
                conn.commit()
            back = int(input("Назад нажмите: 1"))
            if back == 1:
                menu()
            else:
                sys.exit()

        case 4:
            sql_join1 = f""" SELECT rooms_name,price, price*0.9 AS discount, child, client_name, 
COUNT(*) FROM history_orders 
JOIN clients ON clients.client_id = history_orders.fk_client_id 
JOIN rooms ON rooms.rooms_id = fk_room_id
GROUP BY rooms_name,price,child,client_name HAVING COUNT(*) >1;;
 """
            cur.execute(sql_join1)
            # print(cur.execute(sql_update))
            records = cur.fetchall()
            # print(records)
            for row in records:
                # print(row)
                print(f'Номер: {row[0]}, Цена: {row[1]}, Цена со скидкой: {row[2]} , '
                      f'Наличие детей: {row[3]}, Имя клиента: {row[4]}, Останавливался: {row[5]} ')
            conn.commit()
            back = int(input("Назад нажмите: 1"))
            if back == 1:
                menu()
            else:
                sys.exit()

        case 5:
            sql_join2 = f"""SELECT rooms_name AS номер , capacity AS вместимость,  q_rooms AS кол_во_комнат, TV,
fridge AS холодильник, add_service AS доп_сервис, price AS цена_за_номер, status 
FROM rooms;
"""
            cur.execute(sql_join2)
            # print(cur.execute(sql_update))
            records = cur.fetchall()
            # print(records)
            for row in records:
                print(f'Номер: {row[0]}, Вместимость: {row[1]} человек, Кол-во комнат: {row[2]}, '
                      f'ТВ: {row[3]}, Холодильник: {row[4]}, Доп.сервис: {row[5]}, Цена: {row[6]}, Статус: {row[7]} ')
            conn.commit()
            back = int(input("Назад нажмите: 1"))
            if back == 1:
                menu()
            else:
                sys.exit()

        case 6:
            print("Программа закрыта")
            sys.exit()


# name = str(input("Введите имя клиента: "))
# sql_name_client = f"""SELECT client_id FROM clients WHERE client_name = '{name}'; """
# cur.execute(sql_name_client)
# records = cur.fetchall()
# for row in records:
# # Natasha_Romanoff
#     print(type(row[0]))

menu()
conn.close()