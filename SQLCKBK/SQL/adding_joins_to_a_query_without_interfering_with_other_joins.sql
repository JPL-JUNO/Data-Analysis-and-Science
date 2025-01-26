SELECT e.`ENAME`,
    d.`LOC`
FROM emp e,
    dept d
WHERE e.`DEPTNO` = d.`DEPTNO`;
SELECT e.`ENAME`,
    d.`LOC`,
    eb.`RECEIVED`
FROM emp e
    left JOIN dept d ON e.`DEPTNO` = d.`DEPTNO`
    LEFT JOIN emp_bonus eb ON e.`EMPNO` = eb.empno
ORDER BY 2;
-- 标量子查询
-- 如果 SELECT 列表中的子查询返回多行，那么
-- 将导致错误。
SELECT e.`ENAME`,
    d.`LOC`,
    (
        SELECT eb.`RECEIVED`
        FROM emp_bonus eb
        WHERE eb.`EMPNO` = e.`EMPNO`
    ) as received
FROM emp e,
    dept d
WHERE e.`DEPTNO` = d.`DEPTNO`
ORDER BY 2;