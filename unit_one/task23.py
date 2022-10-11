# todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.

# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

unknown_text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin"
letters_en_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_en_dwn = letters_en_up.lower()

for num in range(1, len(letters_en_dwn)+1):
    lst = []
    for i in unknown_text:
        if i in letters_en_dwn:
            lst.append(letters_en_dwn[letters_en_dwn.index(i)-num])
        else:
            lst.append(i)
    print(num, "".join(lst))
