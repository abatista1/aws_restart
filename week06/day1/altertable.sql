-- change the phone column type
/*
ALTER TABLE mydb.users
MODIFY COLUMN phone INTEGER;
*/

-- change the primary key to start from 6 digits 100000
ALTER TABLE mydb.users AUTO_INCREMENT = 100000;