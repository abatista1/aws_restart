#!/bin/bash
#RDS management script


function createdb(){
	echo
}

function startdb(){
	echo
}

function describedb(){
	echo
}

function stopdb(){
	echo
}

function deletedb(){
	echo
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
