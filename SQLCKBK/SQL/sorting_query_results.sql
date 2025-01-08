SELECT `ENAME`,
    `JOB`,
    `SAL`
FROM emp
WHERE `DEPTNO` = 10
ORDER BY `SAL` ASC;
SELECT *
FROM emp
WHERE `DEPTNO` = 10
ORDER BY `SAL` DESC;
SELECT `ENAME`,
    `JOB`,
    `SAL`
FROM emp
WHERE `DEPTNO` = 10
ORDER BY 3 DESC;
SELECT `EMPNO`,
    `DEPTNO`,
    `SAL`,
    `ENAME`,
    `JOB`
FROM emp
ORDER BY `DEPTNO`,
    `SAL` DESC;
SELECT `ENAME`,
    `JOB`
FROM emp
ORDER BY SUBSTR(`JOB`, LENGTH(`JOB`) -1);
SELECT `ENAME`,
    `JOB`
FROM emp
ORDER BY SUBSTRING(`JOB`, LENGTH(`JOB`) -1, 2);
CREATE VIEW v AS
SELECT CONCAT(`ENAME`, ' ', `DEPTNO`) AS DATA
FROM emp;
SELECT *
FROM V;
SELECT DATA
FROM V
ORDER BY REPLACE(
        `DATA`,
        REPLACE(
            TRANSLATE(DATA, '0123456789', '##########'),
            '#',
            ''
        ),
        ''
    );
SELECT `ENAME`,
    `SAL`,
    `COMM`
FROM emp
ORDER BY 3;
SELECT `ENAME`,
    `SAL`,
    `COMM`
FROM emp
ORDER BY 3 DESC;
SELECT `ENAME`,
    `SAL`,
    `COMM`
FROM (
        SELECT `ENAME`,
            `SAL`,
            `COMM`,
            CASE
                WHEN `COMM` IS NULL THEN 0
                ELSE 1
            END AS is_null
        FROM emp
    ) x
ORDER BY is_null DESC,
    `COMM`;
-- control whether NULL values are sorted first or last without interfering with non-NULL values
-- For oracle
SELECT `ENAME`,
    `SAL`,
    `COMM`
FROM emp
ORDER BY `COMM` NULLS LAST;
SELECT `ENAME`,
    `SAL`,
    `COMM`
FROM emp
ORDER BY `COMM` NULLS FIRST;
SELECT `ENAME`,
    `SAL`,
    `JOB`,
    `COMM`
FROM emp
ORDER BY CASE
        WHEN `JOB` = 'SALESMAN' THEN 1
        ELSE 0
    END DESC,
    `COMM`,
    `SAL`;