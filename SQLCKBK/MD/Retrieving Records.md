# 检索记录

## 将 `NULL` 转换为实际值

使用函数 `COALESCE` 将 `NULL` 值替换为实际值。函数 `COALESCE` 可以将一个或多个值作为参数，并返回参数列表中的第一个非 `NULL` 值。

```sql
SELECT COALESCE(`COMM`, 0)
FROM emp;
```

处理 `NULL` 值时，最好利用 DBMS 提供的内置功能。在很多情况下，有多个函数可以很好地完成这项任务，但 `COALESCE` 在所有 DBMS 中都管用。另外，在所有 DBMS 中，都可以使用 `CASE` 来完成这项任务。

```sql
SELECT CASE
        WHEN `COMM` IS NOT NULL THEN `COMM`
        ELSE 0
    END
FROM emp;
```

虽然可以使用 `CASE` 将 NULL 值转换为实际值，但使用 `COALESCE` 更容易且更简洁。
