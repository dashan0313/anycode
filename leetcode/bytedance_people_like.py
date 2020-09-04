为了不断优化推荐效果，今日头条每天要存储和处理海量数据。
假设有这样一种场景：我们对用户按照它们的注册时间先后来标号，
对于一类文章，每个用户都有不同的喜好值，
我们会想知道某一段时间内注册的用户（标号相连的一批用户）中，
有多少用户对这类文章喜好值为k。因为一些特殊的原因，
不会出现一个查询的用户区间完全覆盖另一个查询的用户区间(不存在L1<=L2<=R2<=R1)。

50%

n = int(input())
nums = list(map(int,list(input().split())))
z = int(input())
for _ in range(z):
    qury = list(map(int,list(input().split())))
    i,j = qury[0]-1,qury[1]-1
    count = 0
    for node in range(i,j+1):
        if nums[node] == qury[2]:
            count += 1
    print(count)
