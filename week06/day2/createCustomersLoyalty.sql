-- drop database if exists bookstoredb;
-- drop database mydb;

-- Create the loyalty database
create database if not exists loyalty;

-- Create the customers table
create table if not exists loyalty.customers(
	ID integer primary key not null auto_increment,
    familyName varchar(40) not null,
    givenName varchar(40) not null,
    loyaltyNum integer not null,
    contactNumber varchar(20) not null,
    email varchar(50) not null,
    points integer not null
);

-- Describe the customers table
describe loyalty.customers;
