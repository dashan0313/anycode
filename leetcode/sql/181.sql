# Write your MySQL query statement below
#800ms
select a.Name as Employee from Employee a
where a.Salary > (select c.Salary from Employee c where c.Id = a.ManagerId)

# Write your MySQL query statement below
#200ms
SELECT
     a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
     ON a.ManagerId = b.Id
     AND a.Salary > b.Salary
;
