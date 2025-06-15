insert
    all when loc in ('New Work', 'Boston') then into dept_east (deptno, dname, loc)
VALUES (deptno, dname, loc) when loc = ('Chicago') then into dept_mid (deptno, dname, loc)
VALUES (deptno, dname, loc) else into dept_west (deptno, dname, loc)
VALUES (deptno, dname, loc)
SELECT deptno, dname, loc
from dept;

create table dept_east (
    deptno integer,
    dname VARCHAR(10),
    loc VARCHAR(10) check (loc in ('New Work', 'Boston'))
)
create table dept_mid (
    deptno integer,
    dname VARCHAR(10),
    loc VARCHAR(10) check (loc = 'Chicago')
)
create table dept_west (
    deptno integer,
    dname VARCHAR(10),
    loc VARCHAR(10) check (loc = 'Dallas')
)
insert into (
        select *
        from dept_east
        union all
        select *
        from dept_mid
        union all
        select *
        from dept_west
    )
select *
from dept;