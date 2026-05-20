# Sistema de Controle de Estoque

## Informacoes do projeto

**Nome dos integrantes:** preencher com os nomes dos integrantes do grupo  
**Turma:** preencher com a turma  
**Tema escolhido:** controle de estoque de produtos  
**Linguagem utilizada:** Python  
**Banco de dados utilizado:** SQLite

## Descricao do software

Este software e um sistema simples de controle de estoque executado pelo terminal.
Ele permite consultar produtos cadastrados, buscar produtos pelo nome, listar
produtos por categoria, calcular o valor total do estoque e inserir novos
produtos no banco de dados.

O projeto foi desenvolvido com Python para a logica da aplicacao e SQLite para
armazenar as informacoes de produtos e categorias.

## Organizacao do codigo

```text
project-py-stock-example/
├── data_base/
│   └── main.py
├── source_code/
│   ├── inventory.db
│   └── script.sql
└── README.md
```

### `data_base/main.py`

Arquivo principal do sistema. Nele estao as funcoes responsaveis por conectar
ao banco de dados, exibir o menu e executar as operacoes escolhidas pelo usuario.

Principais funcoes:

- `connect()`: abre a conexao com o banco SQLite.
- `list_products()`: lista todos os produtos cadastrados.
- `search_product()`: busca produtos pelo nome informado.
- `list_by_category()`: lista produtos de uma categoria escolhida.
- `calculate_total_stock()`: calcula o valor total dos produtos em estoque.
- `insert_product()`: cadastra um novo produto.
- `menu()`: exibe o menu principal e controla a navegacao do usuario.

### `source_code/script.sql`

Arquivo SQL usado para criar as tabelas do banco de dados e inserir dados
iniciais de categorias e produtos.

### `source_code/inventory.db`

Arquivo do banco de dados SQLite utilizado pelo programa.

## Desenvolvimento passo a passo

1. Definicao do tema

   O tema escolhido foi um sistema de controle de estoque, com foco em produtos,
   categorias, quantidade disponivel e valor em estoque.

2. Modelagem do banco de dados

   Foram definidas duas tabelas principais: `categories` e `products`.
   A tabela de produtos possui uma chave estrangeira para relacionar cada
   produto a uma categoria.

3. Criacao do script SQL

   Foi criado o arquivo `source_code/script.sql`, contendo os comandos para
   criar as tabelas e inserir registros iniciais no sistema.

4. Criacao do banco SQLite

   A partir do script SQL, foi criado o arquivo `source_code/inventory.db`,
   que armazena os dados usados pela aplicacao.

5. Desenvolvimento da conexao com o banco

   No arquivo `data_base/main.py`, foi criada a funcao `connect()`, responsavel
   por abrir a conexao com o banco de dados SQLite.

6. Desenvolvimento das consultas

   Foram implementadas funcoes para listar produtos, pesquisar produtos pelo
   nome, listar produtos por categoria e calcular o valor total do estoque.

7. Desenvolvimento do cadastro

   Foi criada a opcao de inserir novos produtos, informando nome, preco,
   quantidade e categoria.

8. Criacao do menu

   Foi criado um menu interativo no terminal para permitir que o usuario escolha
   as operacoes do sistema de forma simples.

9. Organizacao final da entrega

   Os arquivos foram organizados em pastas separadas para codigo Python, banco
   de dados, script SQL e documentacao.

## Descricao das tabelas

### Tabela `categories`

Armazena as categorias dos produtos.

| Campo | Tipo | Descricao |
| --- | --- | --- |
| `id_category` | INTEGER | Identificador unico da categoria |
| `category_name` | TEXT | Nome da categoria |

Exemplos de categorias cadastradas: Informatica, Perifericos, Eletronicos,
Acessorios e Escritorio.

### Tabela `products`

Armazena os produtos do estoque.

| Campo | Tipo | Descricao |
| --- | --- | --- |
| `id_product` | INTEGER | Identificador unico do produto |
| `name` | TEXT | Nome do produto |
| `price` | REAL | Preco unitario do produto |
| `quantity` | INTEGER | Quantidade disponivel em estoque |
| `category_id` | INTEGER | Identificador da categoria do produto |

## Opcoes do menu

Ao executar o programa, o usuario visualiza o seguinte menu:

```text
====== INVENTORY CONTROL SYSTEM ======
1 - List all products
2 - Search product by name
3 - List products by category
4 - Calculate total stock value
5 - Insert new product
0 - Exit
```

Descricao das opcoes:

- **1 - List all products:** mostra todos os produtos cadastrados, com ID, nome,
  preco, quantidade e categoria.
- **2 - Search product by name:** permite pesquisar produtos pelo nome ou parte
  do nome.
- **3 - List products by category:** mostra as categorias disponiveis e lista os
  produtos da categoria escolhida.
- **4 - Calculate total stock value:** calcula o valor total do estoque,
  multiplicando preco por quantidade de cada produto.
- **5 - Insert new product:** cadastra um novo produto no banco de dados.
- **0 - Exit:** encerra o sistema.

## Instrucoes para executar o programa

1. Abra o terminal na pasta do projeto.

2. Entre na pasta onde esta o arquivo principal:

   ```bash
   cd data_base
   ```

3. Execute o programa com Python:

   ```bash
   python3 main.py
   ```

4. Escolha uma das opcoes exibidas no menu.

## Observacao

Para recriar o banco de dados a partir do script SQL, execute o comando abaixo
na raiz do projeto:

```bash
sqlite3 source_code/inventory.db < source_code/script.sql
```

# Inventory Control System

## Project Information

**Team members:** fill in the names of the group members  
**Class:** fill in the class  
**Chosen topic:** product inventory control  
**Programming language:** Python  
**Database used:** SQLite

## Software Description

This software is a simple inventory control system executed through the terminal.
It allows the user to list registered products, search for products by name,
list products by category, calculate the total stock value, and insert new
products into the database.

The project was developed using Python for the application logic and SQLite to
store product and category information.

## Code Organization

```text
project-py-stock-example/
├── data_base/
│   └── main.py
├── source_code/
│   ├── inventory.db
│   └── script.sql
└── README.md
```

### `data_base/main.py`

Main file of the system. It contains the functions responsible for connecting
to the database, displaying the menu, and executing the operations selected by
the user.

Main functions:

- `connect()`: opens the connection with the SQLite database.
- `list_products()`: lists all registered products.
- `search_product()`: searches for products by the informed name.
- `list_by_category()`: lists products from a selected category.
- `calculate_total_stock()`: calculates the total value of products in stock.
- `insert_product()`: registers a new product.
- `menu()`: displays the main menu and controls user navigation.

### `source_code/script.sql`

SQL file used to create the database tables and insert initial category and
product records.

### `source_code/inventory.db`

SQLite database file used by the program.

## Development Step by Step

1. Topic definition

   The chosen topic was an inventory control system focused on products,
   categories, available quantity, and total stock value.

2. Database modeling

   Two main tables were defined: `categories` and `products`. The products table
   has a foreign key to relate each product to a category.

3. SQL script creation

   The file `source_code/script.sql` was created with the commands needed to
   create the tables and insert initial records into the system.

4. SQLite database creation

   Based on the SQL script, the file `source_code/inventory.db` was created to
   store the data used by the application.

5. Database connection development

   In the file `data_base/main.py`, the `connect()` function was created to open
   the connection with the SQLite database.

6. Query development

   Functions were implemented to list products, search products by name, list
   products by category, and calculate the total stock value.

7. Product registration development

   The option to insert new products was created, allowing the user to inform
   the name, price, quantity, and category.

8. Menu creation

   An interactive terminal menu was created so the user can choose the system
   operations in a simple way.

9. Final delivery organization

   The files were organized into separate folders for Python code, database,
   SQL script, and documentation.

## Table Description

### `categories` Table

Stores the product categories.

| Field | Type | Description |
| --- | --- | --- |
| `id_category` | INTEGER | Unique category identifier |
| `category_name` | TEXT | Category name |

Examples of registered categories: Informatics, Peripherals, Electronics,
Accessories, and Office.

### `products` Table

Stores the inventory products.

| Field | Type | Description |
| --- | --- | --- |
| `id_product` | INTEGER | Unique product identifier |
| `name` | TEXT | Product name |
| `price` | REAL | Product unit price |
| `quantity` | INTEGER | Available stock quantity |
| `category_id` | INTEGER | Identifier of the product category |

## Menu Options

When the program is executed, the user sees the following menu:

```text
====== INVENTORY CONTROL SYSTEM ======
1 - List all products
2 - Search product by name
3 - List products by category
4 - Calculate total stock value
5 - Insert new product
0 - Exit
```

Option description:

- **1 - List all products:** shows all registered products with ID, name, price,
  quantity, and category.
- **2 - Search product by name:** allows the user to search for products by full
  name or part of the name.
- **3 - List products by category:** shows the available categories and lists the
  products from the selected category.
- **4 - Calculate total stock value:** calculates the total stock value by
  multiplying the price by the quantity of each product.
- **5 - Insert new product:** registers a new product in the database.
- **0 - Exit:** closes the system.

## Instructions to Run the Program

1. Open the terminal in the project folder.

2. Enter the folder where the main file is located:

   ```bash
   cd data_base
   ```

3. Run the program with Python:

   ```bash
   python3 main.py
   ```

4. Choose one of the options displayed in the menu.

## Note

To recreate the database from the SQL script, run the command below from the
project root:

```bash
sqlite3 source_code/inventory.db < source_code/script.sql
```
