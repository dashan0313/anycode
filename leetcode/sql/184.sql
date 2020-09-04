# Write your MySQL query statement below
#部门工资最高的员工
#一开始用了left join，但是有的员工没有部门信息
select D.Name as Department,E.Name as Employee,E.Salary
from Employee E, Department D
where  E.DepartmentId = D.Id
and
(E.Salary,E.DepartmentId) in (select max(Salary),DepartmentId from Employee group by DepartmentId)


#利用开窗函数牛逼，https://www.cnblogs.com/koushr/p/5873407.html
#但是仅限于工资没有重复的情况
-- 每个部门前2高
SELECT S.NAME, S.EMPLOYEE, S.SALARY
  FROM (SELECT D.NAME,
               T.NAME EMPLOYEE,
               T.SALARY,
               ROW_NUMBER() OVER(PARTITION BY T.DEPARTMENTID ORDER BY T.SALARY DESC) RN
          FROM EMPLOYEE T
          LEFT JOIN DEPARTMENT D
            ON T.DEPARTMENTID = D.ID) S
            #主要目的是获取RN这个列
 WHERE S.RN <= 2

 -- 每个部门第一第三高
SELECT S.NAME, S.EMPLOYEE, S.SALARY
  FROM (SELECT D.NAME,
               T.NAME EMPLOYEE,
               T.SALARY,
               ROW_NUMBER() OVER(PARTITION BY T.DEPARTMENTID ORDER BY T.SALARY DESC) RN
          FROM EMPLOYEE T
          LEFT JOIN DEPARTMENT D
            ON T.DEPARTMENTID = D.ID) S
 WHERE S.RN = 1 OR S.RN = 3
