1 - Cree una tabla de Productos, donde se almacenen los siguientes datos:
Código (Es un código alfanumérico).
Nombre.
Precio (Los precios rondan entre los 1000 y 250000).
Fecha de ingreso.
Marca.
COMANDOS PARA CREAR LAS TABLAS
PRODUCTS

CREATE TABLE PRODUCTS (
ID INT PRIMARY KEY,
CODE VARCHAR(15) NOT NULL,
NAME VARCHAR(25) NOT NULL,
PRICE SMALLINT DEFAULT 0,
DATE VARCHAR(15) NOT NULL
CHECK(DATE LIKE "____-__-__"),
BRAND VARCHAR(25) NOT NULL
);
COMANDOS PARA POBLAR TABLA PRODUCTS
INSERT INTO PRODUCTS (CODE, NAME, PRICE, DATE, BRAND)
VALUES
("A001", "Computer", 1000, "2024-01-01", "Dell"),
("A002", "TV", 1000, "2024-01-01", "Sony"),
("B001", "Bed", 1200, "2024-05-20", "Dream"),
("B002", "Stove", 1500, "2024-05-20", "LG"),
("C001", "Sofas", 2000, "2023-12-01", "IKEA"),
("C002", "Cabinets", 5000, "2024-12-01", "IKEA");


2 - Cree una tabla de Facturas, donde se almacenen los siguientes datos:
Número de factura.
Fecha de la compra.
Correo del comprador.
Monto total.
INVOICES
CREATE TABLE INVOICES(
ID INTEGER PRIMARY KEY,
N VARCHAR(15)NOT NULL,
DATE VARCHAR(15) NOT NULL
CHECK(DATE LIKE"____-__-__"),
E_MAIL VARCHAR(30) NOT NULL,
TOTAL INTEGER NOT NULL
);
INVOICES DATA
INSERT INTO INVOICES(N, DATE, E_MAIL, TOTAL)
VALUES
("001", "2024-01-01", "pedropablo@hotmail.com", 32000),
("002", "2024-02-01", "Juanjose@gmail.com", 28000),
("003", "2024-05-25", "mariajose@yahoo.com", 12000),
("004", "2024-01-30", "carlosjuanes@hotmail.com", 10000),
("005", "2025-02-05","alfredomedina@gmail.com", 57500);

3 - Busque la manera de que en cada factura puedan haber varios productos con los siguientes datos:
Cantidad comprada.
Monto total.
INVOICE DETAILS
CREATE TABLE INVOICE_DETAILS(
ID INTEGER PRIMARY KEY,
QUANTITY_PURCHASED SMALLINT NOT NULL,
TOTAL_AMOUNT INTEGER NOT NULL,
PRODUCT_ID INTEGER REFERENCES PRODUCTS (ID),
INVOICE_ID INTEGER REFERENCES INVOICES (ID)
);
INVOICE DETAILS DATA
INSERT INTO INVOICE_DETAILS(QUANTITY_PURCHASED, TOTAL_AMOUNT, PRODUCT_ID, INVOICE_ID)
VALUES
(10, 20000, 5, 1),
(5, 6000, 3, 3),
(10, 10000, 1, 2),
(10, 50000, 6, 5),
(10, 10000, 2, 4),
(10, 10000, 2, 2),
(5, 7500, 4, 5),
(10, 12000, 3, 1),
(4, 8000, 5, 2),
(3, 6000, 5, 3)


4 - Cree una tabla de Carrito de Compras, donde se almacene el email del usuario y los productos que tiene agregados en su carrito.
USERS
CREATE TABLE USERS (
ID INTEGER PRIMARY KEY,
E_MAIL VARCHAR(30) NOT NULL
);
USERS DATA
INSERT INTO USERS (E_MAIL)
VALUES
("pedropablo@hotmail.com"),
("Juanjose@gmail.com"),
("mariajose@yahoo.com"),
("carlosjuanes@hotmail.com"),
("alfredomedina@gmail.com");
SHOPPING CART
CREATE TABLE SHOPPING_CART (
ID INTEGER PRIMARY KEY,
PRODUCT_ID INTEGER REFERENCES PRODUCTS(ID),
USER_ID INTEGER REFERENCES USERS(ID),
QUANTITY SMALLINT NOT NULL
);
SHOPPING CART DATA
INSERT INTO SHOPPING_CART (PRODUCT_ID, USER_ID, QUANTITY)
VALUES
(5, 1, 10),
(3, 3, 5),
(1, 2, 10),
(6, 5, 10),
(2, 4, 10),
(2, 2, 10),
(4, 5, 5),
(3, 1, 10),
(5, 2, 4),
(5, 3, 3);


5 - Agregar tabla de Usuarios y su historial de compras
Cree una tabla de Usuarios que incluya:
ID de usuario (autonumérico)
Nombre completo
Correo (único)
Fecha de registro
MODIFICANDO LA TABLA USER CON MAS COLUMNAS
ALTER TABLE USERS
ADD FULL_NAME VARCHAR(25);
ALTER TABLE USERS
ADD R_DATE VARCHAR(25);
LLENANDO LAS FILAS VACIAS DE LAS COLUMNAS RECIEN CREADAS
UPDATE USERS SET
FULL_NAME= "Pedro Pablo Escobar",
R_DATE= "2023-07-01"
WHERE ID=1;
UPDATE USERS SET
FULL_NAME= "Juan Jose Lopez",
R_DATE="2023-08-20"
WHERE ID=2;
UPDATE USERS SET
FULL_NAME= "Maria Jose Martinez",
R_DATE= "2024-01-01"
WHERE ID=3;
UPDATE USERS SET
FULL_NAME= "Carlos Juanes",
R_DATE="2023-03-20"
WHERE ID=4;
UPDATE USERS SET
FULL_NAME="Alfredo Medina",
R_DATE="2024-11-16"
WHERE ID=5;
MODIFICANDO LA TABLA INVOICES CON UNA COLUMNA QUE REFERENCIA FK
ALTER TABLE INVOICES
ADD USER_ID INTEGER REFERENCES USERS(ID);
LLENADO LAS FILAS DE LA COLUMNA CREADA
UPDATE INVOICES SET
USER_ID=1
WHERE ID=1;
UPDATE INVOICES SET
USER_ID=2
WHERE ID=2;
UPDATE INVOICES SET
USER_ID=3
WHERE ID=3;
UPDATE INVOICES SET
USER_ID=4
WHERE ID=4;
UPDATE INVOICES SET
USER_ID=5
WHERE ID=5;


6 - Crear una tabla de reseñas de productos
Cree una tabla Reseñas que contenga:
ID reseña
Código de producto
Comentario
Calificación (1 al 5)
Fecha
CREANDO UNA NUEVA TABLA DE REVIEWS DONDE REFERENCIARA A PRODUCTOS Y USUARIOS
CREATE TABLE REVIEWS (
ID INTEGER PRIMARY KEY,
P_CODE VARCHAR(20) NOT NULL,
COMMENT VARCHAR(50),
QUALIFICATION VARCHAR(5) NOT NULL,
DATE VARCHAR(10)
CHECK (DATE LIKE "____-__-__"),
PRODUCT_ID INTEGER REFERENCES PRODUCTS(ID),
USER_ID INTEGER REFERENCES USERS(ID)
);
LLENANDO LOS DATOS DE LA TABLA CREADA
INSERT INTO REVIEWS (P_CODE, COMMENT, QUALIFICATION, DATE, PRODUCT_ID, USER_ID)
VALUES
("B001", "Very Comfortable", "★★★★", "2024-05-26", 3, 3),
("C002", "Very little space", "★★", "2025-02-06", 6, 5),
("A001", "The best buy", "★★★★★", "2024-02-02", 1, 2),
("B002", "I love it", "★★★★★", "2025-02-06", 4, 5),
("C001", "Too soft", "★★★", "2024-01-02", 5, 1),
("A002", "It wasn´t what I expected", "★", "2024-02-01", 2, 4);


7 - Agregar soporte para métodos de pago
Cree una tabla de Métodos de Pago:
ID del método
Tipo de método (ej: tarjeta, sinpe, paypal)
Nombre del banco (si aplica)
Relacione cada Factura con su método de pago
CREANDO LA TABLA
CREATE TABLE PAYMENT_METHOD (
ID INTEGER PRIMARY KEY,
METHOD_TYPE VARCHAR(25) NOT NULL
);
LLENANDO LOS DATOS DE LA TABLA ANTERIOR
INSERT INTO PAYMENT_METHOD (METHOD_TYPE)
VALUES
("Credit/Debit Cards"),
("E-Wallets"),
("COD"),
("Cryptocurrencies");
MODIFICANDO LA TABLA INVOICES AGREGANDO LA COLUMNA QUE REFERENCIA LA TABLA DE METODOS DE PAGO COMO FK
ALTER TABLE INVOICES
ADD PAYMENT_MET_ID INTEGER REFERENCES PAYMENT_METHOD(ID);
LLENANDO LA COLUMNA CREADA PARA LAS FK DE LOS METODOS DE PAGO
UPDATE INVOICES SET
PAYMENT_MET_ID=1
WHERE ID=1;
UPDATE INVOICES SET
PAYMENT_MET_ID=2
WHERE ID=2;
UPDATE INVOICES SET
PAYMENT_MET_ID=2
WHERE ID=3;
UPDATE INVOICES SET
PAYMENT_MET_ID=1
WHERE ID=4;
UPDATE INVOICES SET
PAYMENT_MET_ID=3
WHERE ID=5;
EJERCICIOS DE SELECT
Obtenga todos los productos almacenados
SELECT NAME
FROM PRODUCTS;
Obtenga todos los productos que tengan un precio mayor a 1200
SELECT NAME, PRICE
FROM PRODUCTS
WHERE PRICE > 1200;
Obtenga todas las compras de un mismo producto por id.
SELECT *
FROM INVOICE_DETAILS
WHERE PRODUCT_ID=5
Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT
P.NAME AS "PRODUCT",
SUM(ID.QUANTITY_PURCHASED) AS "Total Unidades Compradas"
FROM
PRODUCTS AS P
JOIN
INVOICE_DETAILS AS ID ON P.ID = ID.PRODUCT_ID
GROUP BY
P.NAME;
Obtenga todas las facturas realizadas por el mismo comprador
SELECT
N AS "Nº Factura",
DATE AS "Fecha",
TOTAL AS "Monto Total"
FROM
INVOICES
WHERE
USER_ID = 2;
Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT
N AS "Nº Factura",
TOTAL AS "Monto Total",
DATE AS "Fecha"
FROM
INVOICES
ORDER BY
TOTAL DESC;
Obtenga una sola factura por número de factura.
SELECT *
FROM
INVOICES
WHERE
N = '003