
select ID, givenName, points, email
from loyalty.customers
where ID > 5
group by givenName
having points <= 500
order by givenName desc;