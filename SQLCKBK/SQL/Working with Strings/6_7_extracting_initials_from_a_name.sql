-- Active: 1743238396785@@127.0.0.1@5432@smeagol@public
select replace(
        replace(
            translate(
                REPLACE('Stephen Cui', '.', ''), 'abcdefghijklmnopqrstuvwxyz', rpad('#', 26, '#')
            ), '#', ''
        ), ' ', '.'
    ) || '.'
from t1;