SELECT table_name
FROM information_schema.tables
WHERE
    `TABLE_SCHEMA` = 'smeagol';

SELECT tabname from syscat.tables WHERE tabschema = 'smeagol';

select table_name from all_tables where owner = 'smeagol';