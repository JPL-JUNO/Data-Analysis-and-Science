create view V as
select ename as data
from emp
where
    deptno = 10
union all
select ename || ', $' || cast(sal as char(4)) || '.00' as data
from emp
where
    deptno = 20
union all
select ename || cast(deptno as char(4)) as data
from emp
where
    deptno = 30;

SELECT length(data) from V;

SELECT data
from v
where
    translate(
        lower(data),
        '0123456789abcdefghijklmnopqrstuvwxyz',
        rpad('a', 36, 'a')
    ) = rpad('a', length(data), 'a')