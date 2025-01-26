DROP VIEW IF EXISTS v;
CREATE View V AS
SELECT *
FROM emp
WHERE `DEPTNO` != 10
UNION ALL
SELECT *
FROM emp
WHERE `ENAME` = 'WARD'
SELECT *
FROM v;
SELECT *
FROM (
        SELECT `EMPNO`,
            `ENAME`,
            `JOB`,
            `MGR`,
            `HIREDATE`,
            `SAL`,
            `COMM`,
            `DEPTNO`,
            COUNT(1) AS cnt
        FROM emp e
        GROUP BY `EMPNO`,
            `ENAME`,
            `JOB`,
            `MGR`,
            `HIREDATE`,
            `SAL`,
            `COMM`,
            `DEPTNO`
    ) e
WHERE NOT EXISTS(
        SELECT NULL
        FROM (
                select v.empno,
                    v.ename,
                    v.job,
                    v.mgr,
                    v.hiredate,
                    v.sal,
                    v.comm,
                    v.deptno,
                    count(*) as cnt
                from v
                group by empno,
                    ename,
                    job,
                    mgr,
                    hiredate,
                    sal,
                    comm,
                    deptno
            ) v
        WHERE v.`EMPNO` = e.`EMPNO`
            and v.`ENAME` = e.`ENAME`
            AND v.`JOB` = e.`JOB`
            and COALESCE(v.`MGR`, 0) = COALESCE(e.mgr, 0)
            and v.`HIREDATE` = e.`HIREDATE`
            AND v.sal = e.sal
            AND v.`DEPTNO` = e.`DEPTNO`
            and v.cnt = e.cnt
            AND COALESCE(v.`COMM`, 0) = COALESCE(e.comm, 0)
    )
UNION ALL
SELECT *
FROM(
        select v.`EMPNO`,
            v.`ENAME`,
            v.`JOB`,
            v.`MGR`,
            v.`HIREDATE`,
            v.`SAL`,
            v.`COMM`,
            v.`DEPTNO`,
            COUNT(1) cnt
        FROM v
        GROUP BY v.`EMPNO`,
            v.`ENAME`,
            v.`JOB`,
            v.`MGR`,
            v.`HIREDATE`,
            v.`SAL`,
            v.`COMM`,
            v.`DEPTNO`
    ) V
WHERE NOT EXISTS (
        select null
        FROM(
                select e.`EMPNO`,
                    e.`ENAME`,
                    e.`JOB`,
                    e.`MGR`,
                    e.`HIREDATE`,
                    e.`SAL`,
                    e.`COMM`,
                    e.`DEPTNO`,
                    COUNT(1) cnt
                from emp e
                GROUP BY `EMPNO`,
                    `ENAME`,
                    `JOB`,
                    `MGR`,
                    `HIREDATE`,
                    `SAL`,
                    `COMM`,
                    `DEPTNO`
            ) e
            WHERE v.`EMPNO` = e.`EMPNO`
            and v.`ENAME` = e.`ENAME`
            AND v.`JOB` = e.`JOB`
            and COALESCE(v.`MGR`, 0) = COALESCE(e.mgr, 0)
            and v.`HIREDATE` = e.`HIREDATE`
            AND v.sal = e.sal
            AND v.`DEPTNO` = e.`DEPTNO`
            and v.cnt = e.cnt
            AND COALESCE(v.`COMM`, 0) = COALESCE(e.comm, 0)
    );
