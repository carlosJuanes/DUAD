SET search_path TO lyfter_car_rental;

DROP TABLE IF EXISTS rentals CASCADE;

CREATE TABLE rentals(
id SERIAL PRIMARY KEY,
user_id integer REFERENCES users(id),
car_id integer REFERENCES cars(id),
rental_date DATE DEFAULT CURRENT_DATE,
rental_status VARCHAR(50) CHECK (rental_status IN ('available', 'rented', 'canceled'))
);