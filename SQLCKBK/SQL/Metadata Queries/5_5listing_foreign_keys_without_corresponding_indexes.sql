select fkeys.tabname, fkeys.constname, fkeys.colname, ind_cols.indname (
        select a.tabschema, a.tabname, a.constname, b.colname
        from syscat.tabconst a, syscat.keycoluse b
        where
            a.tabname = 'emp'
            and a.tabschema = 'smeagol'
            and a.type = 'F'
            and a.tabname = b.tabname
            and a.tabschema = b.tabschema
    ) fkeys
    left join (
        select a.tabshcema, a.tabname, a.indname, b.colname
        from syscat.indexes a, syscat.indexcoluse b
        where
            a.indschema = b.indschema
            and a.indname = b.indname
    ) ind_cols on (
        fkeys.tabschema = ind_cols.tabschema
        and fkeys.tabname = ind_cols.tabname
        and fkeys.colname = ind_cols.colname
    )
where
    ind_cols.indname is null;

select a.table_name, a.constraint_name, a.column_name, c.index_name
from
    all_cons_columns a,
    all_constraints b,
    all_ind_columns c
where
    a.table_name = 'EMP'
    and a.owner = 'SMEAGOL'
    and b.constraint_type = 'R'
    and a.owner = b.owner
    and a.table_name = b.table_name
    and a.constraint_name = b.constraint_name
    and a.owner = c.table_owner (+)
    and a.table_name = c.table_name (+)
    and a.column_name = c.column_name (+)
    and c.index_name is null;

select fkeys.table_name, fkeys.constraint_name, fkeys.column_name, ind_cols.indexname
from (
        select a.constraint_schema, a.table_name, a.constraint_name, a.column_name
        from information_schema.key_column_usage a, information_schema.referential_constraints b
        where
            a.constraint_name = b.constraint_name
            and a.constraint_schema = b.constraint_schema
            and a.constraint_schema = 'SMEAGOL'
            and a.table_name = 'EMP'
    ) fkeys
    left join (
        select a.schemaname, a.tablename, a.indexname, b.column_name
        from pg_catalog.pg_indexes a, information_schema.columns b
        where
            a.tablename = b.table_name
            and a.schemaname = b.table_schema
    ) ind_cols on (
        fkeys.constraint_schema = ind_cols.schemaname
        and fkeys.table_name = ind_cols.tablename
        and fkeys.column_name = ind_cols.column_name
    )
where
    ind_cols.indexname is null;

select fkeys.table_name, fkeys.constraint_name, fkeys.column_name, ind_cols.index_name
from (
        select
            a.object_id, d.column_id, a.name table_name, b.name constraint_name, d.name column_name
        from sys.tables a
            join sys.foreign_keys b on (
                a.name = 'EMP'
                and a.object_id = b.parent_object_id
            )
            join sys.foreign_key_columns c on (
                b.object_id = c.constraint_object_id
            )
            join sys.columns d on (
                c.constraint_column_id = d.column_id
                and a.object_id = d.object_id
            )
    ) fkeys
    left join (
        select a.name index_name, b.object_id, b.column_id
        from sys.indexes a, sys.index_columns b
        where
            a.index_id = b.index_id
    ) ind_cols on (
        fkeys.object_id = ind_cols.object_id
        and fkeys.column_id = ind_cols.column_id
    )
where
    ind_cols.index_name is null；