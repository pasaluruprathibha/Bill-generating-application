from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)
# Create table
def init_db():
    conn = sqlite3.connect('bills.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            quantity INTEGER,
            price REAL,
            total REAL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product = request.form['product']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        total = quantity * price

        conn = sqlite3.connect('bills.db')
        c = conn.cursor()
        c.execute('INSERT INTO bills (product, quantity, price, total) VALUES (?, ?, ?, ?)',
                  (product, quantity, price, total))
        conn.commit()
        conn.close()

        return redirect('/bills')
    return render_template('index.html')

@app.route('/bills')
def bills():
    conn = sqlite3.connect('bills.db')
    c = conn.cursor()
    c.execute('SELECT * FROM bills')
    all_bills = c.fetchall()
    conn.close()
    return render_template('bills.html', bills=all_bills)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
