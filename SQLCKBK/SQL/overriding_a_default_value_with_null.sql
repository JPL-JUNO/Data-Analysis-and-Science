DROP TABLE IF EXISTS D;

create table d ( id INTEGER DEFAULT 0, foo VARCHAR(10) );

insert into d (id, foo) VALUES (null, 'Brighten');

insert into d (foo) VALUES ('Brighten');
-- 由于有默认值，因此 id 会显示为 0