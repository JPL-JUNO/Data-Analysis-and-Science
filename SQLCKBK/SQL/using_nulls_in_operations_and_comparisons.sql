SELECT `ENAME`, `COMM`
FROM emp
WHERE
    COALESCE(`COMM`, 0) < (
        SELECT `COMM`
        FROM emp
        WHERE
            `ENAME` = 'WARD'
    )