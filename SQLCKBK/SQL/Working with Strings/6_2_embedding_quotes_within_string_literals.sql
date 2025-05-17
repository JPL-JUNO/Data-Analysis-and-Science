-- Active: 1743238396785@@127.0.0.1@5432@smeagol
select 'g''day mate' qmarks
from t1
union all
select 'beavers'' teeth'
from t1
union ALL
select '''';

select
    'apples core',
    'apple''s core',
    case
        when '' is null then 0
        else 1
    end
from t1;

select '''' as quote from t1;

SELECT '' is null;