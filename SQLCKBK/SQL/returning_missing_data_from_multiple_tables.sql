SELECT d.`DEPTNO`, d.`DNAME`, e.`ENAME`
FROM dept d
    LEFT OUTER JOIN emp e ON d.deptno = e.deptno;
-- 这个员工没有部门
INSERT INTO
    emp (
        empno,
        ename,
        job,
        mgr,
        hiredate,
        sal,
        comm,
        deptno
    )
select 1111, 'YODA', 'JEDI', null, hiredate, sal, comm, null
from emp
where
    ename = 'KING';

SELECT d.`DEPTNO`, d.`DNAME`, e.`ENAME`
FROM dept d
    RIGHT OUTER JOIN emp e ON d.deptno = e.deptno;

-- MySQL does not yet have a FULL OUTER JOIN
SELECT d.`DEPTNO`, d.`DNAME`, e.`ENAME`
FROM dept d FULL OUTER
    JOIN emp e ON d.deptno = e.deptno;

SELECT d.`DEPTNO`, d.`DNAME`, e.`ENAME`
FROM dept d
    LEFT OUTER JOIN emp e ON d.deptno = e.deptno
UNION
SELECT d.`DEPTNO`, d.`DNAME`, e.`ENAME`
FROM dept d
    RIGHT OUTER JOIN emp e ON d.deptno = e.deptno;

-- for Oracle
SELECT d.`DEPTNO`, d.`DNAME`, e.`ENAME`
FROM dept d, emp e
WHERE
    d.`DEPTNO` = e.`DEPTNO` (+)
UNION
SELECT d.`DEPTNO`, d.`DNAME`, e.`ENAME`
FROM dept d, emp e
WHERE
    d.`DEPTNO` (+) = e.`DEPTNO`;
SELECT d.`DEPTNO`, d.`DNAME`, e.`ENAME`
FROM dept d
    LEFT OUTER JOIN emp e ON d.deptno = e.deptno
WHERE
    e.`ENAME` IS NULL;

SELECT d.`DEPTNO`, d.`DNAME`, e.`ENAME`
FROM dept d
    RIGHT OUTER JOIN emp e ON d.deptno = e.deptno
WHERE
    d.`DNAME` IS NULL;