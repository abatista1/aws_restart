select 
sum(points) 'Sum', 
count(points) 'Count', 
round(avg(points),2) 'AVG',
min(points) 'Min',
max(points) 'Max'
from loyalty.customers;