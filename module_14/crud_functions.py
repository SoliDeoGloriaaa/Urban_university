import sqlite3

DB_NAME = 'products.db'


def initiate_db():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products


def populate_db():
    products = [
        ('Product1', 'Описание продукта 1', 100),
        ('Product2', 'Описание продукта 2', 200),
        ('Product3', 'Описание продукта 3', 300),
        ('Product4', 'Описание продукта 4', 400)
    ]
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()


def add_user(username, email, age):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))

    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,))
    count = cursor.fetchone()[0]

    conn.close()

    return count > 0


if __name__ == '__main__':
    initiate_db()
    populate_db()
