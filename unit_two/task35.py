# todo:
# 1. Скачать http-clent https://insomnia.rest/download
# 2. Создать новый проект и установить flask,
# 3. Создать файл requirements.txt  в который занести устанавливаемые библиотеки
# 4. Написать роутеры для REST сервиса/

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
if __name__ == "__main__":
    app.run()
# from markupsafe import escape
# @app.route('/user/<username>')
# def show_user_profile(username):
#
# # show the user profile for that user
#     return f'User {escape(username)}'
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#
# # show the post with the given id, the id is an integer
#     return f'Post {post_id}'
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#
# # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'
    #router /student/{id}
#     def get(self, id):
#         """ Получаем студента по его id """
#         pass
#     #router /student/{id}
#     def post(self):
#         """ Передаем изменения в json """
#
#     # router /student/
#     def put(self):
#         """ Добавить студента в json """
#
#     # router /student/{id}
#     def delete(self):
#         """ Удалим студента по {id}"""
#
#
# 5. Реализовать роутер /student/list - получение списка всех студентов
# студенты могут храниться как в коллекции так и в БД
#
#
# Материал для решения задачи:
# https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html#id11





