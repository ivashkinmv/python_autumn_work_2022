# todo: Убрать повторяющиеся буквы и лишние символы
# Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
# Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

# Input             	            Output
#
# apple	                        aple
# 25.04.2022 Good morning !!	    godmrni


letters_en_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_en_dwn = letters_en_up.lower()

text = """apple
25.04.2022 Good morning !!"""

file = open("apple.txt", "wt+", encoding="utf-8")
file.write(text)

file.seek(0)

result_lst = []
for line in file.readlines():
    for let_lne in line.rstrip():
        for letter in letters_en_dwn:
            if let_lne.lower() == letter:
                if let_lne not in result_lst:
                    result_lst.append(let_lne.lower())
    if "\n" in line:
        result_lst.append("\n\t")

print("".join(result_lst))
