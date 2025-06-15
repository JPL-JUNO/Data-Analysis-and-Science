create table new_sal (deptno int, sal int);

INSERT INTO new_sal (deptno, sal) VALUES (10, 4000);

SELECT deptno, ename, sal, comm from emp order by 1;

update emp s set(e.sal, e.comm) = (
    select ns.sal, ns.sal / 2
    from new_sal ns
    where
        ns.deptno = e.deptno
)
where
    exists (
        select *
        from new_sal ns
        where
            ns.deptno = e.deptno
    );

update emp e,
new_sal ns
set
    e.sal = ns.sal,
    e.comm = ns.sal / 2
where
    e.deptno = ns.deptno;

update (
    select
        e.sal as emp_sal,
        e.comm as emp_comm,
        ns.sal as ns_sal,
        ns.sal / 2 as ns_comm
    from emp e, new_sal ns
    where
        e.deptno = ns.deptno
)
set
    emp_sal = ns_sal,
    emp_comm = ns_comm;

update emp
set
    sal = ns.sal,
    comm = ns.sal / 2
from new_sal ns
where
    ns.deptno = emp.deptno;