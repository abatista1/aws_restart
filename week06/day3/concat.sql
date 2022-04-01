select concat(givenName,' ' , familyName) 'Name',
concat(substring(givenName,1,1),'. ' , substring(familyName,1,1)) 'Initial'
from loyalty.customers