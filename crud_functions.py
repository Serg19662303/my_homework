import sqlite3

def initiate_db(n):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    )
    ''')

    for i in range(1, n + 1):
        cursor.execute('INSERT INTO Products(title, description, price) VALUES(?, ?, ?)',
            (f"Продукт {i}", f"Описание {i}", str(100 * i)))

    connection.commit()
    connection.close()

def get_all_products(i):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    connection.commit()
    connection.close()

    return products[i-1]
