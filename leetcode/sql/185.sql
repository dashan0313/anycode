部门工资前三高的所有员工

select D.Name as Department, e1.Name as Employee, e1.Salary
from
    Employee e1 join Department D on e1.DepartmentId = D.Id
where
    3 >
        (select count(distinct e2.Salary)
            from Employee e2 join Department D on e2.DepartmentId = D.Id
            where e2.Salary > e1.Salary And e2.DepartmentId = e1.DepartmentId)
