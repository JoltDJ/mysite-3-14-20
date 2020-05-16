import sqlite3  
conn = sqlite3.connect('myshop.db')
def createProducts():
  c = conn.cursor()
  sql = """
    CREATE TABLE products (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      price REAL NOT NULL,
      qty INTEGER NOT NULL
  )
"""
c.execute(sql)

def insertProducts():
sql = """
  INSERT INTO products (name, price, qty)
  VALUES (?, ?, ?)
"""
c.execute(sql, ('Pen', 15, 45))
c.execute(sql, ('Cup', 80, 5))
c.execute(sql, ('Notebook', 25, 20))

def listProducts():
    c = conn.cursor()
    sql = "SELECT id, name, price, qty FROM products"
    c.execute(sql)
    print(c.fetchall())

listProducts()