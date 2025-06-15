-- Active: 1743238352364@@127.0.0.1@3306@sqlckbk
create view new_emps as select empno, ename, job from emp;

insert into
    new_emps (empno, ename, job)
values (1, 'Jonathan', 'Editor');