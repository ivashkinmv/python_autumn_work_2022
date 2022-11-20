CREATE TABLE clients
(
	client_id BIGSERIAL PRIMARY KEY,
	client_name VARCHAR(50) NOT NULL,
	email	VARCHAR (50),
	child bool
	
);


CREATE TABLE rooms
(
	rooms_id BIGSERIAL PRIMARY KEY,
	rooms_name int NOT NULL,
	capacity int NOT NULL,
	q_rooms int NOT NULL,
	TV bool,
	fridge bool,
	add_service bool NOT NULL,
	status VARCHAR(50) NOT NULL,
	price real,
	client_id int	
);


CREATE TABLE history_orders
(
	orders_id BIGSERIAL PRIMARY KEY,
	fk_client_id int REFERENCES,
	fk_room_id int REFERENCES 
);


ALTER TABLE history_orders ADD CONSTRAINT fk_client_id
FOREIGN KEY (fk_client_id) REFERENCES clients(client_id)
ON DELETE RESTRICT;


ALTER TABLE history_orders ADD CONSTRAINT fk_rooms_id
FOREIGN KEY (fk_room_id) REFERENCES rooms(rooms_id)
ON DELETE RESTRICT;

ALTER TABLE rooms ADD CONSTRAINT fk_clients_id
FOREIGN KEY (client_id) REFERENCES clients(client_id)
ON DELETE RESTRICT;

INSERT INTO clients
VALUES
(1,'Alex_First', 'AF@gmail.com'),
(2,'Sofia Vergara', 'SV@gmail.com'),
(3, 'Adam Sandler', 'Adam_S@yahoo.com'),
(4, 'Natasha_Romanoff', 'BlackWidow@avengers.com')

INSERT INTO rooms
VALUES
(1, 1001,1,1,'True','True','True', 'Availible',150.0),
(2, 1002,2,1,'True','True','True', 'Occupied',250.0),
(3, 1003,2,2,'True','True','True', 'Booked', 300.5),
(4, 1004,1,2,'True','True','True', 'Availible',200.1),
(5, 1005,1,1, 'True','False','False', 'Availible', 110.0),
(6, 1006,1,1,'False','False','False','Availible',100.0)


INSERT INTO history_orders
VALUES
(1,1,3)

INSERT INTO history_orders
VALUES

(2,2,1)

INSERT INTO history_orders
VALUES

(3,2,1)

INSERT INTO history_orders
VALUES

(4,2,1)