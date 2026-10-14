SET search_path TO ejercicio_1_postgres;
	--MODIFICAION= se removio esta parte del codigo del DO $$ hacia el inicio
	--				para que se ejecute una sola vez y evitar errores
	--				en ejecuciones posteriores
	-- SE ACTUALIZARA LA TABLA BILL  YA QUE NO CUENTO CON 
	-- UNA COLUMNA STATE QUE ME PERMITA AGREGAR EL ESTADO DE LA 
	--FACTURA COMO LO REQUIERE EL EJERCICIO. 
	ALTER TABLE BILLS
	ADD COLUMN STATE VARCHAR(20)DEFAULT 'SUCCESSFUL';
	
DO $$
DECLARE
	--CREACION DE VARIABLES TEMPORALES PARA EL EJERCICIO.
	v_bill_id INTEGER :=4;-- MODIFICACION= se le dio el valor del id a eliminar
	v_current_bill RECORD;				  -- de manera manual para mayor dinamismo
	v_bill_status VARCHAR(20);			  -- evitando crear un bloque de codigo estatico.

BEGIN
		
	IF v_bill_id IS NULL THEN
		RAISE EXCEPTION 'THE BILL IS NOT FOUND';
	END IF;

	-- MODIFICACION= se crea una variable temporal para almacenar el status
	--				 de la factura validarlo y evitar duplicar el stock. 
	SELECT STATE INTO v_bill_status
	FROM bills
	where id= v_bill_id;
	
	IF v_bill_status = 'RETURNED' THEN
		RAISE EXCEPTION 'The bill has already been returned.';
	END IF;
	
	FOR v_current_bill IN
		SELECT *
		FROM BILLS_DETAIL
		WHERE BILL_ID = v_bill_id
	LOOP
		UPDATE PRODUCTS 
		SET QUANTITY=QUANTITY + v_current_bill.QUANTITY_PURCHASED
		WHERE ID =v_current_bill.PRODUCT_ID;
	END LOOP;

	UPDATE BILLS
	SET STATE='RETURNED'
	WHERE ID = v_bill_id;

END $$;