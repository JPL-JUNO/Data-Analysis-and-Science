select replace(
        replace(
            translate(
                REPLACE('Stephen Cui', '.', ''), 'abcdefghijklmnopqrstuvwxyz', rpad('#', 26, '#')
            ), '#', ''
        ), ' ', '.'
    ) || '.'
from t1;