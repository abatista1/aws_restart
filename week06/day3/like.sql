select Name, lower(Name) as Lower, upper(Name) as Upper
from university.students
where lower(Name) like 'a%';