#!/bin/bash
#RDS management script

echo -n "Use DB: "
read db

function createdb(){
	echo -n "Username: "
	read admin
	echo -n "Password: "
	read password
	aws rds create-db-instance --db-instance-identifier $db --db-instance-class db.t3.micro --engine mysql --master-username $admin --master-user-password $password --allocated-storage 20 | grep -wie 'DBInstanceIdentifier' -wie 'DBInstanceClass' -wie 'Engine' -wie 'DBInstanceStatus' -wie 'MasterUSerName' -wie 'Address' | sed 's/^[ \t]*//' | sed 's/,//'
	if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAIL
	fi
}

function startdb(){
	aws rds start-db-instance --db-instance-identifier $db | grep -wie 'DBInstanceIdentifier' -wie 'DBInstanceClass' -wie 'Engine' -wie 'DBInstanceStatus' -wie 'MasterUSerName' -wie 'Address' | sed 's/^[ \t]*//' | sed 's/,//'
	if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAIL
	fi
}

function describedb(){
	aws rds describe-db-instances --db-instance-identifier $db | grep -wie 'DBInstanceIdentifier' -wie 'DBInstanceClass' -wie 'Engine' -wie 'DBInstanceStatus' -wie 'MasterUSerName' -wie 'Address' | sed 's/^[ \t]*//' | sed 's/,//'
}

function stopdb(){
	aws rds stop-db-instance --db-instance-identifier $db | grep -wie 'DBInstanceIdentifier' -wie 'DBInstanceClass' -wie 'Engine' -wie 'DBInstanceStatus' -wie 'MasterUSerName' -wie 'Address' | sed 's/^[ \t]*//' | sed 's/,//'
	if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAIL
	fi
}

function deletedb(){
	aws rds delete-db-instance --db-instance-identifier $db --skip-final-snapshot | grep -wie 'DBInstanceIdentifier' -wie 'DBInstanceClass' -wie 'Engine' -wie 'DBInstanceStatus' -wie 'MasterUSerName' -wie 'Address' | sed 's/^[ \t]*//' | sed 's/,//'
	if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAIL
	fi
}

function helpmenu(){
	echo "\nWelcome to RDS Management System: "
	echo "C - Create RDS mysql instance."
	echo "S - Start RDS mysql instance"
	echo "s - Stop RDS mysql instance"
	echo "d - Describe RDS mysql instance"
	echo "D - Delete RDS mysql instance"
	echo "X - Exit"
}

echo -n "RDS command (C/S/s/d/D/X): "
read op

while [ "$op" != "X" ]
do
	case $op in
		"C")createdb
		;;
		"S")startdb
		;;
		"s")stopdb
		;;
		"d")describedb
		;;
		"D")deletedb
		;;
		*)helpmenu
		;;
	esac
	echo -n "RDS command (C/S/s/d/D/X): "
	read op
done
