import psycopg2
from random import randint

conn = psycopg2.connect(
    host="localhost",
    database="wordle",
    user="postgres",
    password="162657")

cur = conn.cursor()
sql_tuple = f"""SELECT * FROM words"""
cur.execute(sql_tuple)
records = cur.fetchall()

x = randint(1, len(records))

# cur = conn.cursor()
sql_word = f"""SELECT words FROM words WHERE client_id = {x}"""
cur.execute(sql_word)
records = cur.fetchall()


for row in records:
    row_one = row[0]
    print(row_one)
conn.commit()
conn.close()

wordle = row_one
input_word = str(input("Слово из 5ти букв: "))
answer = input_word.lower()

# let1 = str(input("B1: "))
# let2 = str(input("B2: "))
# let3 = str(input("B3: "))
# let4 = str(input("B4: "))
# let5 = str(input("B5: "))
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
