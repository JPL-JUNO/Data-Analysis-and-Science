show index from emp;

select a.tabname, b.indname, b.colname, b.colseq
FROM syscat.indexes a, syscat.indexcoluse b
where
    a.tabname = 'emp'
    AND a.tabschema = 'smeagol'
    and a.indschema = b.indschema
    and a.indename = b.indname;

select
    table_name,
    index_name,
    column_name,
    column_position
from sys.all_ind_columns
where
    table_name = 'emp'
    and table_owner = 'smeagol';

select a.tablename, a.indexname, b.column_name
from pg_catalog.pg_indexes a, information_schema.columns b
WHERE
    a.schemaname = 'smeagol'
    and a.tablename = b.table_name;

select
    a.name table_name,
    b.name index_name,
    d.name column_name,
    c.index_column_id
from sys.tables a, sys.indexes b, sys.index_columns c, sys.columns d
where
    a.object_id = b.object_id
    and b.object_id = c.object_id
    and b.index_id = c.index_id
    and c.object_id = d.object_id
    and c.column_id = d.column_id
    and a.name = 'emp';