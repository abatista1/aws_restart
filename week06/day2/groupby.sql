/*
	GROUP BY example: grouping data by givenName for customers with points > 1000
*/

select ID, givenName, points, email
from loyalty.customers
group by givenName;