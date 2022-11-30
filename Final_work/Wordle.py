import psycopg2
from random import randint
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

# # create the extension
# db = SQLAlchemy()
# # create the app
# app = Flask(__name__)
# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:162657@localhost:5432/wordle'
# db.init_app(app)
#
#
# class Words(db.Model):
#     __tablename__ = "words"
#     id = db.Column(db.Integer, primary_key=True)
#     words = db.Column(db.String, unique=True, nullable=False)
#
#
# with app.app_context():
#     db.create_all()

conn = psycopg2.connect(
    host="localhost",
    database="wordle",
    user="postgres",
    password="162657")
#
cur = conn.cursor()
sql_tuple = f"""SELECT words FROM words"""
cur.execute(sql_tuple)
records = cur.fetchall()

id_x = randint(1, len(records))

cur = conn.cursor()
sql_word = f"""SELECT words FROM words WHERE id = {id_x}"""
cur.execute(sql_word)
records = cur.fetchone()
wordle = records[0]
print(wordle)

input_word = str(input("Слово из 5ти букв: "))
answer = input_word.lower()

"""Заготовка побуквенно"""
# # let1 = str(input("B1: "))
# # let2 = str(input("B2: "))
# # let3 = str(input("B3: "))
# # let4 = str(input("B4: "))
# # let5 = str(input("B5: "))


def game():
    lst = []
    if wordle != answer:
        for letter in answer:
            if letter in wordle:
                if wordle.index(letter) != answer.index(letter):
                    lst.append(letter.upper())
                else:
                    lst.append("'")
                    lst.append(letter.upper())
                    lst.append("'")
            else:
                lst.append(letter)
    else:
        for ltr in answer:
            lst.append("'")
            lst.append(ltr.upper())
            lst.append("'")
    print("".join(lst))


def compare_with_db():
    global answer
    global cur
    # cur = conn.cursor()
    sql_request = f"SELECT words FROM words WHERE words = '{answer}';"
    cur.execute(sql_request)
    records2 = cur.fetchone()
    if records2 == answer:
        game()
    else:
        print("В базе такого слова нет")
    conn.close()


compare_with_db()




"""Формирование базы слов для PostgresQL"""
# file = open(f'C:\python_autumn_2022\Final_work\engwords.txt', 'rt+', encoding='utf-8')
# file_create = open("base_words_sql1.sql", "w", encoding="utf-8")
# file = open(f'base_words.txt', 'rt', encoding='utf-8')
# for row in file:
#     word = row.rstrip()
#     # word = row
#     # if len(word) == 5:
#     file_create.write(f"INSERT INTO words (words) VALUES ('{word}');\n")
#     # file_create.write('\n')
#         # file_create.write(word)
#
#     print(word)
#
# file_create.close()
# file.close()
"""Конец. Формирование базы слов для PostgresQL"""

# if __name__ == "__main__":
#     app.run()
