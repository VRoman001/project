from flask import Flask,render_template
import sqlite3
import random
app = Flask(__name__)


def connect_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM test")
    rows = cursor.fetchall()

    result = []
    for r in rows:
        dictionary = {
            'name': r[0]
        }
        result.append(dictionary)
    conn.close()
    return result
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/paig')
def paig1():
    return render_template('paig.html')

@app.route('/paig2')
def paig2():
    n = connect_db()
    return render_template('paig2.html', recepts = n)

if __name__ == '__main__':
    app.run()


