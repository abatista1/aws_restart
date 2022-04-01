select Name, Grade, Mark
from university.students
where Name regexp '^C+.*x$';