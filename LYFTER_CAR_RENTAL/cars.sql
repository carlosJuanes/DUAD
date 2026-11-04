SET search_path TO lyfter_car_rental;

DROP TABLE IF EXISTS cars CASCADE;
create table cars (
	id SERIAL PRIMARY KEY,
	vin_number VARCHAR(50),
	make VARCHAR(50),
	model VARCHAR(50),
	year VARCHAR(50),
	car_status VARCHAR(20) CHECK (car_status IN ('rented', 'available', 'disabled'))
);


insert into cars (vin_number, make, model, year, car_status) values ('JM1NC2LF1D0662054', 'Toyota', 'Camry', 1999, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('WBABD53486P617863', 'Pontiac', 'Gemini', 1988, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('JHMFA3F29BS348158', 'Pontiac', 'GTO', 2006, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('5FPYK1F28BB837974', 'Ford', 'Explorer Sport', 2001, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('SALAB2D48DA379006', 'Pontiac', 'Torrent', 2007, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('ZHWGU5BZ5AL951085', 'Saab', '9-3', 2003, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('3D7JV1EP7BG718909', 'BMW', 'Z4', 2008, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('WAUEH74F16N992082', 'Toyota', 'Avalon', 2011, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('2HNYD2H20AH694401', 'Infiniti', 'I', 1997, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('WAUDGAFL9EA628741', 'Hyundai', 'Accent', 2008, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('WBAET37424N699323', 'Mazda', '626', 1999, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('SAJWA4DB6DL050000', 'Ford', 'F-Series Super Duty', 2008, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('3VWML7AJ6EM914974', 'Kia', 'Soul', 2011, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('1G6DW67V180768847', 'Jeep', 'Liberty', 2006, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('JTJBARBZ6F2004909', 'Audi', 'RS 4', 2008, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('JH4CU2F45DC502416', 'Jaguar', 'XK Series', 2001, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('WA1CFAFP1BA430780', 'Suzuki', 'SJ 410', 1986, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('5J8TB3H54DL026390', 'Lincoln', 'LS', 2002, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('3VW8S7AT4FM108218', 'Toyota', 'Supra', 1993, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('JN1CV6EK6DM112573', 'Mercury', 'Grand Marquis', 2001, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('JM3TB2BA8F0750495', 'Ford', 'E350', 2012, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('WBAKA4C50BC591708', 'Saab', '9-5', 2005, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('3C63DRHLXCG437208', 'Mitsubishi', 'Galant', 1994, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('19UUA75617A338324', 'Kia', 'Amanti', 2006, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('WAUAH98E38A283255', 'Mazda', 'MPV', 2005, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('3D7TT2CT8BG005070', 'Lamborghini', 'Countach', 1990, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('WBAVB33566A300523', 'Porsche', '928', 1990, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('WAUDFAFL6DA216150', 'Chevrolet', 'Silverado 1500', 2009, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('SALFP2BG3FH494756', 'Audi', '100', 1991, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('WUAAU34209N002596', 'Ford', 'Focus', 2009, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('3D7LT2ET4BG605923', 'Subaru', 'Loyale', 1991, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('137FA90301E776089', 'Mitsubishi', 'Montero', 1996, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('WBAKG7C5XCE509618', 'Volvo', 'V40', 2004, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('WBAKE5C54BE752768', 'Mitsubishi', 'Diamante', 2003, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('YV1672MSXB2864956', 'Audi', 'Q7', 2011, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('1C4NJPBA5FD903604', 'Acura', 'Legend', 1994, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('3D73M4CL7AG866974', 'Audi', 'TT', 2011, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('3C63DRHL5CG791234', 'Cadillac', 'Seville', 1998, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('1C3CDFBA0DD765609', 'Hummer', 'H1', 1997, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('WAUGL98E77A483854', 'Mercedes-Benz', 'C-Class', 2000, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('WUALNAFG3EN498765', 'Chevrolet', 'Suburban 1500', 2002, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('WAUVT58EX2A094991', 'BMW', 'M Roadster', 2008, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('1GD311CG0FZ745551', 'Honda', 'Accord', 2003, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('2HNYD28648H560066', 'Land Rover', 'LR3', 2006, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('1N6AA0CJ7DN283508', 'Lexus', 'IS-F', 2011, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('WBAHN83586D217627', 'Porsche', 'Boxster', 2010, 'rented');
insert into cars (vin_number, make, model, year, car_status) values ('WBAYM9C58ED366711', 'Jaguar', 'XJ', 2006, 'available');
insert into cars (vin_number, make, model, year, car_status) values ('SCBZU25E91C663646', 'Pontiac', 'G6', 2009, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('JN1CV6EK3AM253094', 'Nissan', 'Sentra', 2011, 'disabled');
insert into cars (vin_number, make, model, year, car_status) values ('SCFEBBBKXBG196647', 'Pontiac', 'Grand Prix', 2007, 'rented');
