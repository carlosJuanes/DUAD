-- Obtenga todos los productos almacenados
SELECT NAME FROM PRODUCTS;

-- Obtenga todos los productos que tengan un precio mayor a 1200
SELECT NAME, PRICE
FROM PRODUCTS
WHERE PRICE > 1200;

-- Obtenga todas las compras de un mismo producto por id.
SELECT *
FROM INVOICE_DETAILS
WHERE PRODUCT_ID=5;

-- Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT
P.NAME AS "PRODUCT",
SUM(ID.QUANTITY_PURCHASED) AS "Total Unidades Compradas"
FROM
PRODUCTS AS P
JOIN
INVOICE_DETAILS AS ID ON P.ID = ID.PRODUCT_ID
GROUP BY
P.NAME;

-- Obtenga todas las facturas realizadas por el mismo comprador
SELECT
N AS "Nº Factura",
DATE AS "Fecha",
TOTAL AS "Monto Total"
FROM
INVOICES
WHERE
USER_ID = 2;

-- Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT
N AS "Nº Factura",
TOTAL AS "Monto Total",
DATE AS "Fecha"
FROM
INVOICES
ORDER BY
TOTAL DESC;

-- Obtenga una sola factura por número de factura.
SELECT *
FROM
INVOICES
WHERE
N = '003';

-- Verificación final de productos (ejercicio que realizamos)
SELECT *
FROM PRODUCTS
ORDER BY ID ASC LIMIT 10;