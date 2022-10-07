# todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

# Содержимое файла import_this.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# выходные данные
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.
file = open("import_this.txt", "w+")
a = "Beautiful is better than ugly."
b = "Explicit is better than implicit."
c = "Simple is better than complex."
d = "Complex is better than complicated."
text = a + "\n" + b + "\n" + c + "\n" + d
file.write(text)
file.close()

file = open("import_this.txt", "r")
lst = []
for i in file.readlines():
    if "\n" in i:
        lst.append(i.rstrip("\n"))
        # lst.append(i[0:len(i)-1]) # Или так
    if "\n" not in i:
        lst.append(i)
for j in lst[::-1]:
    print(j)
file.close()
