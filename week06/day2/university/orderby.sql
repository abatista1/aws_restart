select * from university.students
where Grade="HD" or Grade="D"
group by Name
order by Name desc;