-- Active: 1743238352364@@127.0.0.1@3306@sqlckbk
SELECT empno from emp_bonus;

update emp
set
    sal = sal * 1.2
where
    empno in (
        select empno
        from emp_bonus
    );

UPDATE EMP
SET
    SAL = SAL * 1.2
WHERE
    EXISTS (
        SELECT NULL
        FROM emp_bonus
        WHERE
            EMP.`EMPNO` = emp_bonus.`EMPNO`
    );

SELECT NULL,`EMP`.*
FROM emp_bonus, `EMP
WHERE
    EMP.`EMPNO` = emp_bonus.`EMPNO`