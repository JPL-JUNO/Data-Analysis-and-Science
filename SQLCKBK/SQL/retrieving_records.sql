SELECT *
FROM emp;
SELECT *
FROM emp
WHERE DEPTNO = 10;
SELECT *
FROM emp
WHERE `DEPTNO` = 10
    OR `COMM` IS NOT NULL
    OR `SAL` <= 2000
    AND `DEPTNO` = 20;
SELECT `ENAME`,
    `DEPTNO`,
    `SAL`
FROM emp;
SELECT sal AS salary,
    comm AS commission
FROM emp;
SELECT sal AS salary,
    comm AS commission
FROM emp
WHERE salary < 5000;
SELECT *
FROM (
        SELECT sal AS salary,
            comm AS commission
        FROM emp
    ) x
WHERE salary < 5000;
SELECT CONCAT(`ENAME`, ' Works as a ', `JOB`) AS msg
FROM emp
WHERE `DEPTNO` = 10;
SELECT `ENAME`,
    `SAL`,
    CASE
        WHEN `SAL` <= 2000 THEN 'UNDERPAID'
        WHEN `SAL` >= 4000 THEN 'OVERPAID'
        ELSE 'OK'
    END AS status
FROM emp;
SELECT *
FROM emp
FETCH FIRST 5 ROWS ONLY;
SELECT *
FROM emp
LIMIT 5;
SELECT *
FROM emp
WHERE ROWNUM <= 5;
SELECT TOP 5 *
FROM emp;
SELECT *
FROM emp
ORDER BY RAND()
FETCH FIRST 5 ROWS ONLY;
SELECT *
FROM emp
ORDER BY RAND()
LIMIT 5;
SELECT *
FROM emp
ORDER BY RANDOM()
LIMIT 5;
SELECT *
FROM(
        SELECT *
        FROM emp
        ORDER BY DBMS_RANDOM.VALUE()
    )
WHERE ROWNUM <= 5;
SELECT TOP 5
FROM emp
ORDER BY NEWID();
SELECT *
FROM emp
WHERE `COMM` IS NULL;
SELECT COALESCE(`COMM`, 0)
FROM emp;
SELECT CASE
        WHEN `COMM` IS NOT NULL THEN `COMM`
        ELSE 0
    END
FROM emp;
SELECT *
FROM emp
WHERE `DEPTNO` IN (10, 20);
SELECT *
FROM emp
WHERE `DEPTNO` IN (10, 20)
    AND (
        `ENAME` LIKE "%I%"
        OR `JOB` LIKE '%ER'
    );