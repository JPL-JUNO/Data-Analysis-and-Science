-- 同时使用外连接和聚合
DROP TABLE if EXISTS emp_bonus;
CREATE TABLE emp_bonus (
    EMPNO INTEGER NOT NULL,
    RECEIVED VARCHAR(12),
    TYPE INT
);

INSERT INTO emp_bonus VALUES (7934, '17-MAR-2005', 1);

INSERT INTO emp_bonus VALUES (7934, '15-FEB-2005 ', 2);

SELECT * FROM emp_bonus;
SELECT
    deptno,
    SUM(`SAL`) AS total_sal,
    SUM(bonus) as total_bonus
FROM (
        SELECT
            e.`EMPNO`, e.`ENAME`, e.`SAL`, e.`DEPTNO`, e.`SAL` * CASE
                WHEN eb.`TYPE` = 1 THEN 0.1
                WHEN eb.`TYPE` = 2 THEN 0.2
                ELSE 0.3
            END AS bonus
        FROM emp e, emp_bonus eb
        WHERE
            e.`EMPNO` = eb.`EMPNO`
            AND e.`DEPTNO` = 10
    ) t
GROUP BY
    `DEPTNO`;

SELECT
    `DEPTNO`,
    SUM(DISTINCT sal) AS total_sal,
    SUM(bonus) AS total_bonus
FROM (
        SELECT
            e.`EMPNO`, e.`ENAME`, e.`SAL`, e.`DEPTNO`, e.`SAL` * CASE
                WHEN eb.`TYPE` = 1 THEN 0.1
                WHEN eb.`TYPE` = 2 THEN 0.2
                ELSE 0.3
            END AS bonus
        FROM emp e
            LEFT OUTER JOIN emp_bonus eb ON e.`EMPNO` = eb.`EMPNO`
        WHERE
            e.`DEPTNO` = 10
    ) t1
GROUP BY
    `DEPTNO`;

SELECT DISTINCT
    `DEPTNO`,
    total_sal,
    total_bonus
FROM (
        SELECT
            e.`EMPNO`, e.`ENAME`, SUM(DISTINCT e.`SAL`) OVER (
                PARTITION BY
                    e.`DEPTNO`
            ) AS total_sal, e.`DEPTNO`, SUM(
                e.`SAL` * CASE
                    WHEN eb.`TYPE` = 1 THEN 0.1
                    WHEN eb.`TYPE` = 2 THEN 0.2
                    ELSE 0.3
                END
            ) OVER (
                PARTITION BY
                    e.`DEPTNO`
            ) AS total_bonus
        FROM emp e
            LEFT OUTER JOIN emp_bonus eb ON e.`EMPNO` = eb.`EMPNO`
        WHERE
            e.`DEPTNO` = 10
    ) t;

SELECT d.deptno, d.total_sal, SUM(
        e.sal * CASE
            WHEN eb.`TYPE` = 1 THEN 0.1
            WHEN eb.`TYPE` = 2 THEN 0.2
            ELSE 0.3
        END
    ) total_bonus
FROM emp e, emp_bonus eb, (
        SELECT `DEPTNO`, SUM(`SAL`) total_sal
        FROM emp
        WHERE
            `DEPTNO` = 10
    ) d
WHERE
    e.`DEPTNO` = d.deptno
    AND e.`EMPNO` = eb.empno
GROUP BY
    d.deptno,
    d.total_sal;