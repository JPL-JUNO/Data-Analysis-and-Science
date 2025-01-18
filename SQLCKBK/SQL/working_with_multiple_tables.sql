SELECT `ENAME` AS ename_and_dname,
    `DEPTNO`
FROM emp
WHERE `DEPTNO` = 10
UNION ALL
SELECT '--------',
    NULL
FROM t1
UNION ALL
SELECT `DNAME`,
    `DEPTNO`
FROM dept;
SELECT e.`ENAME`,
    d.`LOC`
FROM emp e,
    dept d
WHERE e.`DEPTNO` = d.`DEPTNO`
    AND e.`DEPTNO` = 10;
SELECT e.`ENAME`,
    d.`LOC`
FROM emp e,
    dept d;
SELECT e.`ENAME`,
    d.`LOC`
FROM emp e
    INNER JOIN dept d USING(`DEPTNO`)
WHERE d.`DEPTNO` = 10;
CREATE VIEW V AS
SELECT `ENAME`,
    `JOB`,
    `SAL`
FROM emp
WHERE `JOB` = 'CLERK';
SELECT e.`ENAME`,
    e.`EMPNO`,
    e.`JOB`,
    e.`SAL`,
    e.`DEPTNO`
FROM emp e,
    V
WHERE e.`ENAME` = `V`.`ENAME`
    AND e.`JOB` = `V`.`JOB`
    AND e.`SAL` = `V`.`SAL`;
SELECT e.`ENAME`,
    e.`EMPNO`,
    e.`JOB`,
    e.`SAL`,
    e.`DEPTNO`
FROM emp e
    JOIN v ON (
        e.`ENAME` = v.`ENAME`
        AND e.`JOB` = v.`JOB`
        AND e.`SAL` = v.`SAL`
    );
SELECT `EMPNO`,
    `ENAME`,
    `JOB`,
    `SAL`,
    `DEPTNO`
FROM emp
WHERE(`ENAME`, `JOB`, `SAL`) IN(
        SELECT `ENAME`,
            JOB,
            SAL
        FROM emp
        INTERSECT
        /*unsupported in mysql*/
        SELECT `ENAME`,
            JOB,
            SAL
        FROM v
    );
SELECT `DEPTNO`
FROM dept
WHERE `DEPTNO` NOT IN(
        SELECT `DEPTNO`
        FROM emp
    );
SELECT d.`DEPTNO`
FROM dept d
    LEFT JOIN emp e ON d.`DEPTNO` = e.`DEPTNO`
WHERE e.`DEPTNO` IS NULL;