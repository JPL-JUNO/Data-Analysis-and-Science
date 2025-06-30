-- Active: 1743238396785@@127.0.0.1@5432@smeagol@public
DROP VIEW IF EXISTS V69;

CREATE view V69 as (
    SELECT concat(
            e.ename, ' ', cast(e.empno as char(4)), ' ', d.dname
        ) as data
    from emp e, dept d
    WHERE
        e.deptno = d.deptno
);

SELECT * FROM V69;

SELECT data
FROM v69
ORDER BY cast(
        replace(
            translate(
                data, replace(
                    translate(
                        data, '0123456789', '##########'
                    ), '#', ''
                ), rpad('#', 20, '#')
            ), '#', ''
        ) as integer
    );

SELECT data, translate(
        data, '0123456789', '##########'
    )
FROM v69;

SELECT data, replace(
        translate(
            data, '0123456789', '##########'
        ), '#', ''
    )
FROM v69;
-- 不再包含任何数字

SELECT translate(
        data, replace(
            translate(
                data, '0123456789', '##########'
            ), '#', ''
        ), rpad('#', 20, '#')
    )
FROM v69;