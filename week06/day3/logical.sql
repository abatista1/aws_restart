select ID, Name, Mark, Grade
from university.students
where Grade = "HD" and not(Mark>=85);