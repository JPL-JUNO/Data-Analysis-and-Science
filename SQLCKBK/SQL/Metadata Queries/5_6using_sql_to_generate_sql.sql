SELECT 'select count(*) from ' || table_name || ';' cnt
from user_tables;

SELECT CONCAT(
        'select count(*) from ', table_name, ';'
    ) cnt
from information_schema.TABLES
WHERE
    table_schema = 'smeagol';