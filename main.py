from flask import Flask, render_template, request, redirect
import sqlite3
import random
app = Flask(__name__)


def connect_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Recepts, Ingredients, Instruction FROM test")
    rows = cursor.fetchall()

    result = []
    for r in rows:
        dictionary = {
            'Recepts': r[0],
            'Ingredients': r[1],
            'Instuction': r[2]
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

# Маршрут для обробки даних форми
@app.route('/submit', methods=['POST'])
def submit_form():
    recepts = request.form['recipeName']
    ingredients = request.form['ingredients']
    instructions = request.form['instructions']
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO test (Recepts, Ingredients, Instruction) VALUES (?, ?, ?)', (recepts, ingredients, instructions))
        conn.commit()
    
    return redirect("/")

if __name__ == '__main__':
    app.run()
