select Grade, count(Grade) 'Frequency',
concat(round(count(*)*100/sum(count(*)) over(),2),' %') 'Percentage'
-- count(*)*100/(select count(*) from university.students) 'Percentage'
from university.students
group by Grade;