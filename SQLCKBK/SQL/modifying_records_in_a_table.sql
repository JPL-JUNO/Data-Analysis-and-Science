SELECT deptno, ename, sal FROM emp where `DEPTNO` = 20 ORDER BY 1, 3;

update emp set sal = sal * 1.1 where deptno = 20;

SELECT
    `DEPTNO`,
    `ENAME`,
    sal as orig_sal,
    sal * 0.1 amt_to_add,
    sal * 1.1 new_sal
FROM emp
WHERE
    `DEPTNO` = 20
ORDER BY 1, 5;