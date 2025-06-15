select
    column_name,
    data_type,
    ordinal_position
from information_schema.COLUMNS
WHERE
    table_schema = 'smeagol'
    and table_name = 'emp';