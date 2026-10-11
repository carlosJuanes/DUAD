--2) Agrupamiento y conteo cruzado
--Usando las tablas de Books, Customers y Rents:
--Obtenga el número total de veces que cada cliente ha rentado un libro
--Ordene de mayor a menor y limite el resultado a los 3 clientes más activos
--Debe usar: GROUP BY, COUNT(), ORDER BY, LIMIT


--CREACION DE TABLAS PARA LAS CONSULTAS DE LOS EJERCICIOS.
CREATE TABLE AUTHORS(
ID INTEGER PRIMARY KEY,
NAME VARCHAR(50)
);

CREATE TABLE BOOKS(
ID INTEGER PRIMARY KEY,
NAME VARCHAR(50),
AUTHOR INTEGER REFERENCES AUTHORS(ID)
);

CREATE TABLE CUSTOMERS(
ID INTEGER PRIMARY KEY,
NAME VARCHAR(50),
E_MAIL VARCHAR(50)
);

CREATE TABLE RENTS(
ID INTEGER PRIMARY KEY,
BOOKS_ID INTEGER REFERENCES BOOKS(ID),
CUSTOMER_ID INTEGER REFERENCES CUSTOMERS(ID),
STATE VARCHAR(30)
);

--LLENANDO LAS TABLAS PARA LAS CUNSULTAS

INSERT INTO AUTHORS(ID, NAME)
VALUES
(1,	"Miguel de Cervantes"),
(2,	"Dante Alighieri"),
(3,	"Takehiko Inoue"),
(4,	"Akira Toriyama"),
(5,	"Walt Disney");

INSERT INTO BOOKS(ID, NAME, AUTHOR)
VALUES
(1,	"Don Quijote", 1),
(2,	"La Divina Comedia", 2),
(3,	"Vagabond 1-3",	3),
(4,	"Dragon Ball 1", 4),
(5,	"The Book of the 5 Rings", NULL);

INSERT INTO CUSTOMERS(ID, NAME, E_MAIL)
VALUES
(1, "John Doe", "j.doe@email.com"),
(2,	"Jane Doe",	"jane@doe.com"),
(3,	"Luke Skywalker", "darth.son@email.com");

INSERT INTO RENTS(ID, BOOKS_ID, CUSTOMER_ID, STATE)
VALUES
(1,	1,	2,	"Returned"),
(2,	2,	2,	"Returned"),
(3,	1,	1,	"On time"),
(4,	3,	1,	"On time"),
(5,	2,	2,	"Overdue");

--consulta requerida para los ejercicios extras.
SELECT CUSTOMER.NAME, COUNT(RENT.ID) 
FROM CUSTOMERS AS CUSTOMER
LEFT JOIN RENTS AS RENT
ON CUSTOMER.ID=RENT.CUSTOMER_ID
GROUP BY CUSTOMER.NAME
ORDER BY COUNT(RENT.ID) DESC
LIMIT 3

