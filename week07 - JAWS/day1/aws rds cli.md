# AWS CLI Cheatsheet

https://docs.aws.amazon.com/cli/latest/reference/rds/


### Create RDS mysql database instance
```
aws rds create-db-instance
    --db-instance-identifier <instance-name> 
    --db-instance-class db.t3.micro 
    --engine mysql 
    --master-username admin 
    --master-user-password <password> 
    --allocated-storage 20
```

### Describe RDS mysql instance
```
aws rds describe-db-instances
    --db-instance-identifier <instance-name>
```

### Stop RDS mysql instance
```
aws rds stop-db-instance
    --db-instance-identifier <instance-name>
```

### Start RDS mysql instance
```
aws rds start-db-instance
    --db-instance-identifier <instance-name>
```

### Delete RDS mysql instance
```
aws rds delete-db-instance 
--db-instance-identifier <instance-name> 
--skip-final-snapshot
```

### Connect to RDS MySQL using Command Line
```
mysql --user <mymasteruser> --password --host <endpoint>

OR

mysql -h <endpoint> -P 3306 -u <mymasteruser> -p

```

### Create SQL Table
```
CREATE TABLE students(
    ID INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY(START WITH 100000, INCREMENT BY 1),
    "NAME" VARCHAR(255) NOT NULL,
    EMAIL VARCHAR(255) NOT NULL,
    PHONE VARCHAR(255) NOT NULL,
    PRIMARY KEY(ID)
);

```

### Insert Many into SQL Table
```
INSERT INTO university.students("NAME",EMAIL,PHONE)
VALUES
    ('John Smith','john.smith@uts.com','99661100'),
    ('Jane Doe','jane.dh@uts.com','99668800'),
    ('Lucy Lu','lucy@uts.com','99660000'),
    ('Jim Carry','jim.carry@uts.com','88661100');

```
