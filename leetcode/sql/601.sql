
编写一个 SQL 查询以找出每行的人数大于或等于 100 且 id 连续的三行或更多行记录。

返回按 visit_date 升序排列的结果表。
# Write your MySQL query statement below
select distinct a.*
from Stadium a,Stadium b,Stadium c
where ((a.id = b.id - 1 and b.id + 1 = c.id)
    or
    (a.id - 1 = b.id and a.id + 1 = c.id)
    or
    (a.id - 1 = c.id and b.id + 1 = c.id))
    and
    (a.people >= 100 and b.people >= 100 and c.people >= 100)

order by a.id
