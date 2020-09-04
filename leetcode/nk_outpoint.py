P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内（横纵坐标都大于x），
则称其为“最大的”。求出所有“最大的”点的集合。（所有点的横坐标和纵坐标都不重复, 坐标轴范围在[0, 1e9) 内）

如下图：实心点为满足条件的点的集合。请实现代码找到集合 P 中的所有 ”最大“ 点的集合并输出。

#70%通过，一般吧，不够快
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort()  # 先按照x大小排序
res = [data[-1]]  # x最大的肯定是
max_y = data[-1][1]  # 记录最大y
for i in range(len(data)-2, -1, -1):
    y = data[i][1]
    if y>max_y:  # 说明右上区域没点
        max_y = y
        res.append(data[i])
for x, y in res[::-1]:
    print(str(x)+' '+str(y))
