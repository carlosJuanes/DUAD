--Cree la tabla categories con: id (PK autoincrement), name (UNIQUE, NOT NULL), description
-- CREATE TABLE CATEGORIES (
-- ID INTEGER PRIMARY KEY,
-- NAME VARCHAR(25) UNIQUE NOT NULL,
-- DESCRIPTION VARCHAR(50) NOT NULL);

-- Agregue a products la columna category_id (INTEGER, puede permitir NULL)
-- ALTER TABLE PRODUCTS 
-- ADD CATEGORY_ID INTEGER REFERENCES CATEGORIES(ID)

-- Inserte al menos 3 filas en categories
-- INSERT INTO CATEGORIES (NAME, DESCRIPTION)
-- VALUES
-- ("Electronics", "device and consumer electronics components"),
-- ("Furniture", "large and movable article used to make a house habitable"),
-- ("White goods", "large domestic appliance used for household tasks");

-- Actualice algunos products asignándoles un category_id
-- UPDATE PRODUCTS SET
-- CATEGORY_ID=1
-- WHERE ID IN (1,2);

-- UPDATE PRODUCTS SET
-- CATEGORY_ID=2
-- WHERE ID IN (3,5,6);

-- UPDATE PRODUCTS SET
-- CATEGORY_ID=3
-- WHERE ID IN (4);


-- todos los ejercicios anteriores estan comentados porque ya los habia implementado
-- en el entregable anterior la intecion era hacerlos todos juntos pero olvide los
-- siguientes ejercicios para completar todos los ejercicios de SQL



-- Carga de productos y filtros básicos
-- - Inserte al menos 10 filas en products con product_name, price, quantity
INSERT INTO PRODUCTS (CODE, NAME, PRICE, DATE, BRAND, CATEGORY_ID, QUANTITY)
VALUES
("D001", "REFRIGERATOR", 5000, "2025-01-07", "LG", 3, 30),
("D002", "MICRO WAVE", 700, "2025-01-12", "SAMSUNG", 3, 20),
("E001", "TABLE", 3500, "2025-01-12", "GG", 2, 17),
("E002", "DISHWASHER", 3500, "2025-03-24", "SAMSUNG", 3, 14); 

Correcciones de datos en productos
Establezca quantity = 0 donde price <= 0
UPDATE PRODUCTS SET
QUANTITY=0
WHERE PRICE<=0;

-- Aumente el price en 100 unidades para todos los productos cuando quantity sea menor a 10
UPDATE PRODUCTS SET
PRICE =PRICE+100
WHERE QUANTITY<10;

-- Disminuya quantity en 1 para un product_id específico
UPDATE PRODUCTS SET
QUANTITY =QUANTITY-1
WHERE ID =1;



-- Verifique con SELECT * FROM products (muestre id, product_name, price, category_id)
SELECT
ID,
NAME,
PRICE,
CATEGORY_ID
FROM PRODUCTS;

--  -Seleccione todos los productos
SELECT *
FROM PRODUCTS;

--  -Seleccione productos con price > 2000
SELECT *
FROM PRODUCTS
WHERE PRICE>2000;

--  -Seleccione productos cuyo product_name contenga la palabra “apple”   usando LIKE
SELECT *
FROM PRODUCTS
WHERE NAME LIKE "%apple%";
-- = No se encontro ningún producto dentro de mi hoja de inventario con ese nombre 

--  Liste los 5 productos más caros con ORDER BY price DESC LIMIT 5
SELECT *
FROM PRODUCTS
ORDER BY PRICE DESC LIMIT 5;

-- Verifique con SELECT * FROM products ORDER BY id ASC LIMIT 10
SELECT *
FROM PRODUCTS
ORDER BY ID ASC LIMIT 10;
