#编写一个 SQL 查询，查找 Person 表中所有重复的电子邮箱。
#第一次有报错，因为新建的表格没有命名

select Email
from (
    select Email,count(Email) as num
    from Person
    Group by Email
) as stat
where num>1
