select 
count(distinct Language) 'Distinct Language',
count(Language) 'Total Languages'
from world.countrylanguage;