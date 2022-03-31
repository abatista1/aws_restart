create table if not exists university.students(
	ID integer primary key not null,
    Name varchar(100) unique not null,
    Mark integer not null,
    Grade varchar(10) not null
);

describe university.students;