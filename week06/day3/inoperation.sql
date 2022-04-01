select Name, Grade, Mark
from university.students
where Grade in ("D", "HD")
order by Name desc;