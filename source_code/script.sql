CREATE TABLE IF NOT EXISTS categorias (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_categoria TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

INSERT INTO categorias (nome_categoria) VALUES
('Informática'),
('Periféricos'),
('Eletrônicos'),
('Acessórios'),
('Escritório');

INSERT INTO produtos (nome_produto, preco, quantidade, id_categoria) VALUES
('Notebook Lenovo', 3500.00, 5, 1),
('Mouse Gamer', 120.00, 20, 2),
('Teclado Mecânico', 250.00, 15, 2),
('Monitor 24 polegadas', 899.90, 8, 3),
('Cabo HDMI', 35.00, 30, 4),
('Cadeira de Escritório', 650.00, 6, 5),
('Webcam Full HD', 180.00, 10, 3);