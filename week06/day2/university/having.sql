select * from university.students
where Grade="HD"
group by Name
having Mark > 90;
