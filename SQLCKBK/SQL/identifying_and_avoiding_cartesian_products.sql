-- 识别并避免笛卡儿积
SELECT *
FROM emp e,
    dept d
WHERE e.`DEPTNO` = 10;
-- ❌
-- 在这个查询中，使用部门编号 10 对 EMP 表进
-- 行筛选的结果为 3 行。由于没有对 DEPT 表进行筛选，因此
-- 将返回该表的所有行（4 行）。3 乘 4 等于 12，因此这个查
-- 询将返回 12 行数据。
SELECT *
from emp e
where deptno = 10;
SELECT e.ename,
    d.loc
FROM emp e,
    dept d
where e.deptno = 10
    and d.deptno = e.deptno;