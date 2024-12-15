from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

data_name = "database.db"

# функція, яка буде створювати bd, якщо її немає
def init_db():
    if not os.path.exists(data_name):
        with sqlite3.connect(data_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT)
                        ''')
            conn.commit()

@app.route("/")
def login_form():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit_form():
    username = request.form['username']
    password = request.form['password']

    with sqlite3.connect(data_name) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?,?)',(username, password))
        conn.commit()

    return "ДАНІ ЗБЕРЕЖЕНО"


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)

