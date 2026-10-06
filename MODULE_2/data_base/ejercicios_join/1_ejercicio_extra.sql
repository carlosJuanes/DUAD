-- SQLite
CREATE TABLE ALL_NUMBERS(
ID INTEGER PRIMARY KEY,
ALLS INTEGER
);

CREATE TABLE ODD_NUMBERS(
ID INTEGER PRIMARY KEY,
ODDS INTEGER
);

INSERT INTO ALL_NUMBERS(ID, ALLS)
VALUES
(1,	1),
(2,	2),
(3,	3),
(4,	4),
(5,	5),
(6,	6),
(7,	7),
(8,	8),
(9,	9),
(10, 10);

INSERT INTO ODD_NUMBERS(ID, ODDS)
VALUES
(1,	1),
(2,	3),
(3,	5),
(4,	7),
(5,	9);

SELECT ANS.ALLS
FROM ALL_NUMBERS AS ANS
LEFT JOIN ODD_NUMBERS AS ONS
ON ANS.ALLS=ONS.ODDS WHERE ONS.ODDS IS NULL

--1- Explicación cruzada entre conjuntos y SQL
--	- Analice la operación de conjuntos All - Odd.
--	-All - Odd--------------{2,4,6,8,10}
--	R// en la operacion All-Odd a la lista que contiene todos los valores All 
--	se le resta los elementos de la lista Odd dando como resultado 
--	los valores {2,4,6,8,10} que son los mismos numeros de Even = {2,4,6,8,10}
--	- Explique cómo una operación similar se puede representar en SQL con JOINs.
--	-¿Qué tipo de JOIN usaría?
--	R//Para representar una diferencia de valores en dos tablas en SQL aplicariamos 
--	un Left Join para comparar los valores y filtrariamos con un is null para conseguir
--	solo los valores presentes de la tabla primera y de esa manera extraerlos siendo los nulls
--	los que nos interesaria de la segunda tabla.