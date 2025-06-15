CREATE table dept_accidents (
    deptno INTEGER,
    accident_name VARCHAR(20)
);

insert into dept_accidents values (10, 'BROKEN FOOT');

insert into dept_accidents values (10, 'FLESH WOUND');

insert into dept_accidents values (20, 'FIRE');

insert into dept_accidents values (20, 'FIRE');

insert into dept_accidents values (20, 'FLOOD');

insert into dept_accidents values (30, 'BRUISED GLUTE');

SELECT * FROM dept_accidents;

delete from emp
WHERE
    deptno in (
        select deptno
        from dept_accidents
        GROUP BY
            deptno
        HAVING
            COUNT(1) >= 3
    );