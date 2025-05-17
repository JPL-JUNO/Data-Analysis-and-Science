-- Active: 1743238396785@@127.0.0.1@5432@smeagol
select
    ename,
    replace(
        translate(ename, 'AEIOU', 'aaaaa'),
        'a',
        ''
    ) stripped1,
    sal,
    replace(cast(sal as char(4)), '0', '') stripped2
from emp;

-- just for mysql
select ename, replace(
        replace(
            replace(
                replace(
                    replace(ename, 'A', ''), 'E', ''
                ), 'I', ''
            ), 'O', ''
        ), 'U', ''
    ) as stripped1
from emp;