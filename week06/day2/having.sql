/*
	HAVING example: Having clause add more conidition to the select
*/
select ID, givenName, email, points
from loyalty.customers
having points > 1000;