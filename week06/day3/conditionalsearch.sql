select Region, sum(Population)
from world.country
where SurfaceArea > 200000
group by Region
having sum(Population) > 1000000
order by sum(Population) desc limit 5;