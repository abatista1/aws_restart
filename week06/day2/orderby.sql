/*
	ORDER BY example: Order BY allows us to order asc/desc by column(s)
*/

select ID, givenName, email, points
from loyalty.customers
order by ID, givenName desc;