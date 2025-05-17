-- Active: 1743238396785@@127.0.0.1@5432@smeagol
select substr(e.ename, iter.pos, 1) as C
from (
        select ename
        from emp
        where
            ename = 'KING'
    ) e, (
        select id as pos
        from t10
    ) iter
WHERE
    iter.pos <= LENGTH(e.ename);

select substr(e.ename, iter.pos) a, substr(
        e.ename, length(e.ename) - iter.pos + 1
    ) b
FROM (
        select ename
        from emp
        where
            ename = 'KING'
    ) e, (
        select id pos
        from t10
    ) iter
where
    iter.pos <= length(e.ename);