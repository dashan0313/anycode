SELECT id,
SUM(CASE WHEN month='Jan' THEN revenue END) AS Jan_Revenue,
SUM(CASE WHEN month='Feb' THEN revenue END) AS Feb_Revenue,
SUM(CASE WHEN month='Mar' THEN revenue END) AS Mar_Revenue,
SUM(CASE WHEN month='Apr' THEN revenue END) AS Apr_Revenue,
SUM(CASE WHEN month='May' THEN revenue END) AS May_Revenue,
SUM(CASE WHEN month='Jun' THEN revenue END) AS Jun_Revenue,
SUM(CASE WHEN month='Jul' THEN revenue END) AS Jul_Revenue,
SUM(CASE WHEN month='Aug' THEN revenue END) AS Aug_Revenue,
SUM(CASE WHEN month='Sep' THEN revenue END) AS Sep_Revenue,
SUM(CASE WHEN month='Oct' THEN revenue END) AS Oct_Revenue,
SUM(CASE WHEN month='Nov' THEN revenue END) AS Nov_Revenue,
SUM(CASE WHEN month='Dec' THEN revenue END) AS Dec_Revenue
FROM department
GROUP BY id
ORDER BY id;

作者：xxiao053
链接：https://leetcode-cn.com/problems/reformat-department-table/solution/guan-yu-group-byyu-sumde-pei-he-by-xxiao053/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
就以作者意思，可能是CASE WHEN month='Jan' THEN revenue END ，在做着的情况下，一个分组会产生三个值，一个是等于Jan的值，还有两个不等于Jan的值就是null，
如果你没用是sum函数，就是一行需要返回三条数据，但实际可能返回其中一条，那一条不是你需要的。所以使用sum函数,求和，因为加一个null值等于没加，所以三个值变成一个值
