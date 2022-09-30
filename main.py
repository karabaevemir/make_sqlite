import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def create_products(conn, product):
    sql = '''INSERT INTO products (product_title, price, quantity) 
    VALUES(?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def update_products_quantity(conn, id, new_quantity):
    sql = '''UPDATE products SET new_quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_quantity, id))
        conn.commit()
    except Error as e:
        print(e)


def update_products_price(conn, id, new_price):
    sql = '''UPDATE products SET new_price = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_price, id))
        conn.commit()
    except Error as e:
        print(e)


def delete_products(conn, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)
database = r'emir.db'


def select_products(conn):
    try:
        sql = '''SELECT id, product_title, price, quantity FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Error as e:
        print(e)


def select_products_by_price_quantity(conn):
    try:
        sql = '''SELECT id, product_title, price, quantity FROM products WHERE price <= 100 and quantity >= 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print('Selected products by price and quantity:')

        for row in rows:
            print(row)

    except Error as e:
        print(e)


def find_by_product_title(conn):
    try:
        sql = '''select * from products  where product_title LIKE 'beet';'''
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()
        print('The result of your request:')
        for row in rows:
            print(row)

        c.close()
    except Error as e:
        print(e)

sql_create_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
);
'''


connection = create_connection(database)
if connection is not None:
    print('Connected successfully!')
    # create_table(connection, sql_create_table)
    # create_products(connection, ('Sausage', 120, 10))
    # create_products(connection, ('beet', 40, 30))
    # create_products(connection, ('banana', 150, 15))
    # create_products(connection, ('onion', 20, 40))
    # create_products(connection, ('grape', 70, 10))
    # create_products(connection, ('lemon', 140, 20))
    # create_products(connection, ('lemonade', 100, 4))
    # create_products(connection, ('marshmallow', 160, 7))
    # create_products(connection, ('honey ', 90, 15))
    # create_products(connection, ('lollipop', 10, 100))
    # create_products(connection, ('yogurt', 80, 24))
    # create_products(connection, ('kefir', 65, 3))
    # create_products(connection, ('grain', 70, 13))
    # create_products(connection, ('rice', 50, 4))
    # create_products(connection, ('cottage cheese', 40, 11))
    update_products_price(connection, 2, 20)
    select_products(connection)
    select_products_by_price_quantity(connection)
    delete_products(connection, 4)
    find_by_product_title(connection)
    update_products_quantity(connection, 7, 15)
