# todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id - номер по порядку (от 1 до 10);
# – текст из списка algoritm

import csv
algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori",
"EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"]

# Каждое значение из списка должно находится на отдельной строке.

file = open("algoritm.csv", "w", encoding = "UTF-8")
numbers = 1
for i in algoritm:
    strng = str(numbers) + ", " + str(i) + "\n"
    numbers += 1
    file.write(strng)
file.close()
