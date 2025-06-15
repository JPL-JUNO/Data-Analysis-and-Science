-- Active: 1743238352364@@127.0.0.1@3306@sqlckbk
create table dept_2 like dept;

create table dept_2 as SELECT * from dept WHERE 1 = 0;

SELECT * into dept_2 from dept WHERE 1 = 0;