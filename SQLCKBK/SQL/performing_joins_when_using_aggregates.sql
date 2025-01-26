-- 同时使用连接和聚合
DROP TABLE if EXISTS emp_bonus;
CREATE TABLE emp_bonus(
    EMPNO INTEGER NOT NULL,
    RECEIVED VARCHAR(12),
    TYPE INT
);
INSERT INTO emp_bonus
VALUES(7934, '14-MAR-2005', 1);
INSERT INTO emp_bonus
VALUES (7934, '14-MAR-2005', 2);
INSERT INTO emp_bonus
VALUES (7839, '14-MAR-2005', 3);
INSERT INTO emp_bonus
VALUES (7782, '14-MAR-2005', 1);
SELECT *
FROM emp_bonus;
SELECT e.`EMPNO`,
    e.`ENAME`,
    e.`SAL`,
    e.`DEPTNO`,
    e.`SAL` * CASE
        WHEN eb.`TYPE` = 1 THEN 0.1
        WHEN eb.`TYPE` = 2 THEN 0.2
        ELSE 0.3
    END bonus
FROM emp e,
    emp_bonus eb
WHERE e.`EMPNO` = eb.`EMPNO`
    AND `DEPTNO` = 10;
SELECT `DEPTNO`,
    SUM(`SAL`) total_sal,
    SUM(bonus) total_bonus
FROM(
        SELECT e.`EMPNO`,
            e.`ENAME`,
            e.`SAL`,
            e.`DEPTNO`,
            e.`SAL` * CASE
                WHEN eb.`TYPE` = 1 THEN 0.1
                WHEN eb.`TYPE` = 2 THEN 0.2
                ELSE 0.3
            END bonus
        FROM emp e,
            emp_bonus eb
        WHERE e.`EMPNO` = eb.`EMPNO`
            AND `DEPTNO` = 10
    ) x
GROUP BY `DEPTNO`;
-- MILLER 有两次奖金
SELECT *
from emp e,
    emp_bonus eb
WHERE e.`EMPNO` = eb.`EMPNO`;
SELECT `DEPTNO`,
    SUM(DISTINCT `SAL`) total_sal,
    SUM(bonus) total_bonus
FROM(
        SELECT e.`EMPNO`,
            e.`ENAME`,
            e.`SAL`,
            e.`DEPTNO`,
            e.`SAL` * CASE
                WHEN eb.`TYPE` = 1 THEN 0.1
                WHEN eb.`TYPE` = 2 THEN 0.2
                ELSE 0.3
            END bonus
        FROM emp e,
            emp_bonus eb
        WHERE e.`EMPNO` = eb.`EMPNO`
            AND `DEPTNO` = 10
    ) x
GROUP BY `DEPTNO`;
-- ??? 如果有两个不同的员工但是其薪资一样怎么办？岂不是要少算
select d.deptno,
    d.total_sal,
    SUM(
        e.sal * case
            WHEN eb.`TYPE` = 1 then 0.1
            WHEN eb.`TYPE` = 2 then 0.2
            else 0.3
        END
    ) total_bonus
FROM emp e,
    emp_bonus eb,
    (
        select deptno,
            sum(sal) as total_sal
        from emp
        where deptno = 10
        group by deptno
    ) d
WHERE e.`EMPNO` = eb.`EMPNO`
    and e.`DEPTNO` = 10
GROUP BY d.deptno,
    d.total_sal;