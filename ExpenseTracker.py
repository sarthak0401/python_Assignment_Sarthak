from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__, template_folder='template2')
DATABASE = 'expenses.db'


def connect_db():
    return sqlite3.connect(DATABASE)


def create_expenses_table():
    with connect_db() as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                          (id INTEGER PRIMARY KEY,
                           date DATE,
                           amount REAL,
                           category TEXT)''')


@app.before_request
def setup():
    create_expenses_table()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_expense', methods=['POST'])
def add_expense():
    date_str = request.form['date']
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    amount = float(request.form['amount'])
    category = request.form['category']

    with connect_db() as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO expenses (date, amount, category) VALUES (?, ?, ?)", (date, amount, category))
        db.commit()

    return redirect(url_for('index'))


@app.route('/spending_patterns')
def spending_patterns():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    with connect_db() as db:
        cursor = db.cursor()
        if start_date and end_date:
            cursor.execute("SELECT date, category, amount FROM expenses WHERE date BETWEEN ? AND ? ORDER BY date",
                           (start_date, end_date))
        else:
            cursor.execute("SELECT date, category, amount FROM expenses ORDER BY date")
        data = cursor.fetchall()

    return render_template('pattern.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
