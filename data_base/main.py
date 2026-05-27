import sqlite3
import os

DATABASE_PATH = os.path.join(".", "source_code", "inventory.db")

def connect():
    return sqlite3.connect(DATABASE_PATH)

def list_products():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            products.id_product,
            products.name,
            products.price,
            products.quantity,
            categories.category_name
        FROM products
        INNER JOIN categories 
            ON products.category_id = categories.id_category
        ORDER BY products.name;
    """)
    products = cursor.fetchall()
    print("\n--- LIST OF PRODUCTS ---")
    for p in products:
        print(f"ID: {p[0]} | Product: {p[1]} | Price: R$ {p[2]:.2f} | Quantity: {p[3]} | Category: {p[4]}")
    connection.close()

def search_product():
    name = input("Enter product name: ")
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            products.name,
            products.price,
            products.quantity,
            categories.category_name
        FROM products
        INNER JOIN categories 
            ON products.category_id = categories.id_category
        WHERE products.name LIKE ?;
    """, (f"%{name}%",))
    products = cursor.fetchall()
    print("\n--- SEARCH RESULTS ---")
    if products:
        for p in products:
            print(f"Product: {p[0]} | Price: R$ {p[1]:.2f} | Quantity: {p[2]} | Category: {p[3]}")
    else:
        print("No product found.")
    connection.close()

def list_by_category():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT id_category, name FROM categories;")
    categories = cursor.fetchall()
    print("\n--- CATEGORIES ---")
    for c in categories:
        print(f"{c[0]} - {c[1]}")
    category_id = input("Enter category ID: ")
    cursor.execute("""
        SELECT 
            products.name,
            products.price,
            products.quantity
        FROM products
        WHERE products.category_id = ?;
    """, (category_id,))
    products = cursor.fetchall()
    print("\n--- PRODUCTS IN CATEGORY ---")
    if products:
        for p in products:
            print(f"Product: {p[0]} | Price: R$ {p[1]:.2f} | Quantity: {p[2]}")
    else:
        print("No products found in this category.")
    connection.close()

def calculate_total_stock():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT SUM(price * quantity)
        FROM products;
    """)
    total = cursor.fetchone()[0]
    print("\n--- TOTAL STOCK VALUE ---")
    print(f"Total in stock: R$ {total:.2f}")
    connection.close()

def insert_product():
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT id_category, name FROM categories;")
    categories = cursor.fetchall()
    print("\n--- CATEGORIES ---")
    for c in categories:
        print(f"{c[0]} - {c[1]}")
    category_id = int(input("Enter category ID: "))
    cursor.execute("""
        INSERT INTO products 
        (name, price, quantity, category_id)
        VALUES (?, ?, ?, ?);
    """, (name, price, quantity, category_id))
    connection.commit()
    connection.close()
    print("Product inserted successfully!")

def menu():
    while True:
        print("\n====== INVENTORY CONTROL SYSTEM ======")
        print("1 - List all products")
        print("2 - Search product by name")
        print("3 - List products by category")
        print("4 - Calculate total stock value")
        print("5 - Insert new product")
        print("0 - Exit")
        option = input("Choose an option: ")
        if option == "1":
            list_products()
        elif option == "2":
            search_product()
        elif option == "3":
            list_by_category()
        elif option == "4":
            calculate_total_stock()
        elif option == "5":
            insert_product()
        elif option == "0":
            print("Closing the system...")
            break
        else:
            print("Invalid option. Try again.")

menu()
