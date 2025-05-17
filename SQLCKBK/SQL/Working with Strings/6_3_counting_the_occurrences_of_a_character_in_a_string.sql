select (
        length('10,clark,manager') - length(
            replace('10,clark,manager', ',', '')
        )
    ) / length(',')
from t1;
-- 仅当要查找的字符串的长度大于 1 时，这个除法运算才
-- 是必不可少的。

select (
        length('HELLO HELLO') - length(
            replace('hello hello', 'll', '')
        )
    ) / length('ll') correct_cnt,
    length('HELLO HELLO') - length(
        replace('hello hello', 'll', '')
    ) incorrect_cnt;