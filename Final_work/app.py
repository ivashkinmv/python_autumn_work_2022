from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres2:162657@localhost:5432'
db.init_app(app)


class User(db.Model):
    __tablename__ = "user3"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    age = db.Column(db.Integer, nullable=False)
    online = db.Column(db.Boolean, nullable=True)
    # id_account = db.Column(db.ForeignKey('account2.id'))


class Account(db.Model):
    __tablename__ = "account3"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String)
    password = db.Column(db.String)
    # user = db.relationship('User2', backref='account2')


with app.app_context():
    db.create_all()


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# @app.route('/account/create', methods=['GET', 'POST'])
# def account_create():
#     if request.method == 'POST':
#         account = Account(
#             login=request.form["login"],
#             password=request.form["password"],
#         )
#         db.session.add(account)
#         db.session.commit()
#         return "OKey"
#         return redirect(url_for('user_detail', id=user.id))
#
#     return render_template('account.html')
#
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         return "Получили данные"
# #     else:
# #         return "Форма логина"
# #
# #
# # @app.route('/student/list')
# # def get_list():
# #     return {"id": 12, "name": "Peter I"}
# #
# #
# # @app.route('/student/list')
# # def cancel():
# #     return "<span>Ваша песенка спета</span>"


if __name__ == "__main__":
    app.run()
