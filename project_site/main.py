from flask import Flask,render_template
import random
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/paig')
def paig1():
    return render_template('paig.html')

@app.route('/paig2')
def paig2():
    return render_template('paig2.html')

if __name__ == '__main__':
    app.run()

