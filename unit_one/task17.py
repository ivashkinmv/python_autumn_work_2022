# todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
# Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
# Цены хранятся в словаре:
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}
def compute_bill(x):
    s = sum(x.values())
    return s

print(compute_bill(prices))

def compute_bill(x):
    res = 0
    for i in x.values():
        res +=i
    return res
print(compute_bill(prices))