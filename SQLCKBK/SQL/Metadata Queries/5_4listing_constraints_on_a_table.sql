SELECT *
from information_schema.TABLE_CONSTRAINTS a
WHERE
    a.table_schema = 'smeagol'
    and a.table_name = 'emp';

SELECT * from information_schema.KEY_COLUMN_USAGE b;

SELECT a.table_name, a.constraint_name, b.column_name, a.constraint_type
from information_schema.TABLE_CONSTRAINTS a, information_schema.key_column_usage b
WHERE
    a.table_schema = 'smeagol'
    and a.table_name = 'emp'
    and a.table_name = b.table_name
    and a.table_schema = b.table_schema
    and a.`CONSTRAINT_NAME` = b.`CONSTRAINT_NAME`;

-- for db2
select a.tabname, a.constname, b.colname, a.type
from syscat.tabconst a, syscat.columns b
where
    a.tabname = 'emp'
    and a.tabschema = 'smeagol'
    and a.tablename = b.tabname
    and a.tabschema = b.tabschema;

SELECT a.table_name, a.constraint_name, b.column_name, a.constraint_type
FROM
    all_constraints a,
    all_cons_columns b
where
    a.table_name = 'emp'
    and a.owner = 'smeagol'
    and a.table_name = b.table_name
    and a.owner = b.owner
    and a.constraint_name = b.constraint_name;