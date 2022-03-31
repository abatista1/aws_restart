/*
	WHERE example: select all customers where loyalty points are greater than 2000
*/
select ID, givenName, email, points
from loyalty.customers
where points > 2000;
