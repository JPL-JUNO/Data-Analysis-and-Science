select replace(
        translate(
            data, '0123456789', '0000000000'
        ), '0', ''
    ) ename, cast(
        replace(
            translate(
                lower(data), 'abcdefghijklmnopqrstyuwxyz', rpad('z', 26, 'z')
            ), 'z', ''
        ) as integer
    ) as sal
FROM (
        select ename || sal as data
        from emp
    ) x;

select replace(
        translate(
            data, '0123456789', '0000000000'
        ), '0', ''
    ) ename, cast(
        replace(
            translate(
                lower(data), 'abcdefghijklmnopqrstyuwxyz', replicate ('z', 26)
            ), 'z', ''
        ) as integer
    ) as sal
FROM (
        select concat(ename, sal) as data
        from emp
    ) x;