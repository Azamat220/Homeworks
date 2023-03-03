import sqlite3


connection = sqlite3.connect('hw.db')
if connection is not None:
    print('Connected successfully')


connection.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             product_title TEXT NOT NULL,
             price NUMERIC(10, 2) NOT NULL DEFAULT 0.0,
             quantity INTEGER NOT NULL DEFAULT 0)''')


def add_products():
    products = [('Liquid soap', 25.0, 20), ('Baby soap', 20.5, 30), ('Coca-cola', 75.0, 5),
                ('Sprite', 70.5, 45), ('Fanta', 60.5, 65), ('Jamson', 2000.5, 45),
                ('Juice', 50.5, 25), ('Red bull', 120.5, 65), ('Nitro', 60.0, 10),
                ('Sausage', 200.5, 45), ('Milk', 70.5, 65), ('Smoke', 110.0, 1),
                ('Ice cream', 50.0, 10), ('Lays', 120.0, 20), ('Apple', 120.0, 30)]
    connection.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    connection.commit()


def update_quantity(id, quantity):
    connection.execute("UPDATE products SET quantity=? WHERE id=?", (quantity, id))
    connection.commit()

def update_price(id, price):
    connection.execute("UPDATE products SET price=? WHERE id=?", (price, id))
    connection.commit()


def delete_product(id):
    connection.execute("DELETE FROM products WHERE id=?", (id,))
    connection.commit()


def select_all_products():
    cursor = connection.execute("SELECT * FROM products")
    for row in cursor:
        print(row)

def select_cheap_products():
    cursor = connection.execute("SELECT * FROM products WHERE price < 100.0 AND quantity > 5")
    for row in cursor:
        print(row)

def search_products(name):
    cursor = connection.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%' + name + '%',))
    for row in cursor:
        print(row)

connection.close()
