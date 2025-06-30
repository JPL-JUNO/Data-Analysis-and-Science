-- Active: 1743238352364@@127.0.0.1@3306@sqlckbk
SELECT ename FROM emp ORDER BY SUBSTR(`ENAME`, length(ename) -1, 2);