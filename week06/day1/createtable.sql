/*
	create a table in mydb called users if it doesn't exist
    the users table should have (id,fullname,phone,age)
*/

CREATE TABLE IF NOT EXISTS mydb.users(
	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    fullname VARCHAR(40) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    age INTEGER NOT NULL
);