--3) Consulta con múltiples JOINS anidados
--Genere un SELECT que devuelva lo siguiente:
--Nombre del cliente
--Nombre del libro
--Nombre del autor
--Estado del alquiler (Rents.State)
--Debe manejar el caso en que un libro no tenga autor


--Hice este ejercicio partiendo de la tabla de  clientes
--comparandola con la tabla de rentas por lo cual solo me daba los datos
--de los libros que hayan sido rentados omitiendo los no rentados
--y en ese caso no se manejaba el libro que no tenia autor 
--"The Book of the 5 Rings" comno lo requiere el ejercicio. 

--SELECT RENT.ID AS RENT_ID,
--CUSTOMER.NAME AS CUSTOMER_NAME,
--BOOK.NAME AS BOOK_NAME,
--AUTHOR.NAME AS AUTHOR_NAME,
--RENT.STATE
--FROM CUSTOMERS AS CUSTOMER
--LEFT JOIN RENTS AS RENT
--ON CUSTOMER.ID=RENT.CUSTOMER_ID
--LEFT JOIN  BOOKS AS BOOK
--ON RENT.BOOKS_ID=BOOK.ID
--LEFT JOIN AUTHORS AS AUTHOR
--ON BOOK.AUTHOR=AUTHOR.ID
--ORDER BY RENT_ID ASC

--Por lo que cree otro comando donde  se incluyan todos los libros
--para poder trabajar con ese caso especifico, "libro sin autor" para 
--eso tuve que partir la comparacion desde la tabla libros y la tabla
--authors y asi sucesivamente para poder conseguir todos los datos 
--completos de todas las tablas en una sola.
SELECT RENT.ID AS RENT_ID,
CUSTOMER.NAME AS CUSTOMER_NAME,
BOOK.NAME AS BOOK_NAME,
AUTHOR.NAME AS AUTHOR_NAME,
RENT.STATE
FROM BOOKS AS BOOK
LEFT JOIN AUTHORS AS AUTHOR
ON BOOK.AUTHOR=AUTHOR.ID
LEFT JOIN  RENTS AS RENT
ON RENT.BOOKS_ID=BOOK.ID
LEFT JOIN CUSTOMERS AS CUSTOMER
ON CUSTOMER.ID=RENT.CUSTOMER_ID
ORDER BY RENT_ID ASC