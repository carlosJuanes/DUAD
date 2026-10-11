SET search_path TO ejercicio_1_postgres;

DO $$
DECLARE
	-- DECLARANDO VARIABLES TEMPORALES
	V_user_name VARCHAR;
	v_available_stock INTEGER;
	v_current_product RECORD ;
	V_price numeric :=0;
	v_total numeric :=0;

BEGIN
	-- SE CREO UN CARRO DE COMPRAS PREVIO A LA FACTURACION
	--PARA TENER UNA TABLA EN LA QUE ITERAR UNA LISTA DE PRODUCTOS.
	CREATE TABLE shopping_cart(
	ID serial primary key,
	USER_ID integer references users(id),
	PRODUCT_ID integer references products(id),
	QUANTITY integer not null
	);

	INSERT INTO shopping_cart(USER_ID, PRODUCT_ID, QUANTITY)
	VALUES
	(1, 1, 1),
	(1, 2, 1),
	(1, 3, 1);

	--SE VALIDARON LA EXISTENCIA DE EL USUARIO, PRODUCTOS Y STOCK 
	-- DE LA BASE DE DATOS.
	SELECT name INTO V_user_name
	FROM users
	WHERE  id = (SELECT USER_ID FROM shopping_cart LIMIT 1);

	IF V_user_name is null THEN
		RAISE EXCEPTION 'THE USER IS NOT FOUND';
	END IF;

	FOR v_current_product IN
		SELECT *
		FROM shopping_cart
	LOOP
		IF (SELECT ID FROM PRODUCTS WHERE ID = v_current_product.PRODUCT_ID) IS NULL THEN
			RAISE EXCEPTION 'PRODUCT NOT FOUND';
		END IF;

		SELECT quantity INTO v_available_stock
		FROM products 
		where id=  v_current_product.product_id;
		IF v_available_stock IS NULL OR v_available_stock < v_current_product.quantity THEN
			RAISE EXCEPTION 'INSUFICIENT STOCK FOR THE PRODUCT';
		END IF;

	--SE ACTUALIZARA EL STOCK DESPUES DE CADA ITERACION.
		UPDATE products
		SET quantity=quantity - v_current_product.quantity
		where id = v_current_product.product_id;
		
		SELECT PRICE INTO V_price
		FROM PRODUCTS
		WHERE ID = v_current_product.product_id;
		v_total=v_total + v_price * v_current_product.quantity;
	END LOOP;
	
	--SE INGRESO LA FACTURA A LA TABLA DE BILLS
	INSERT INTO BILLS(DATE, USER_ID, TOTAL)
	VALUES
	(now(), v_current_product.user_id, v_total );

END $$;