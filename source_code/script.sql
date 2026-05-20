CREATE TABLE IF NOT EXISTS categories (
    id_category INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id_product INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

INSERT INTO categories (category_name) VALUES
('Informática'),
('Periféricos'),
('Eletrônicos'),
('Acessórios'),
('Escritório');

INSERT INTO products (name, price, quantity, category_id) VALUES
('Notebook Lenovo', 3500.00, 5, 1),
('Mouse Gamer', 120.00, 20, 2),
('Teclado Mecânico', 250.00, 15, 2),
('Monitor 24 polegadas', 899.90, 8, 3),
('Cabo HDMI', 35.00, 30, 4),
('Cadeira de Escritório', 650.00, 6, 5),
('Webcam Full HD', 180.00, 10, 3);