import sqlite3

conn = sqlite3.connect('db/ecommerce.db')  # path to your database
cursor = conn.cursor()

# Create a simple products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')

# Insert sample data (optional)
cursor.execute('''
INSERT INTO products (name, description, price, stock)
VALUES
    ('Product 1', 'A cool product', 199.99, 10),
    ('Product 2', 'Another cool product', 299.99, 5)
''')

conn.commit()
conn.close()
