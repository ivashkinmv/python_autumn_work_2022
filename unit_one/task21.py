# todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""
file_create = open("index.html", "w", encoding="utf-8")
file_create.write(template)
file_create.close()

file_change = open("index.html", "r+", encoding="utf-8")
for i in file_change.readlines():
    loop = 0
    for k, v in page.items():
        if k in i:
            loop = 1
            splt = i.split("?")
            jn = (splt[0] + v + splt[1]).rstrip()
            print(jn)
    if loop == 0:
        print(i.rstrip())
