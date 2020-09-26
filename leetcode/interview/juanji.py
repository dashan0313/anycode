在图像处理中，卷积是常用的技术，现有P(h,w)的的图片，像素值为[0, 255]的整数。卷积核为K(m, m)的矩阵，元素值为[0, 1.]的浮点数，输出图像大小为O(h - m + 1, w - m + 1)，其中h>=m, w>=m。卷积后中的图片O元素值计算如下，其中最后的输出像素值为向下取整的整数



现输入图片P和卷积核K，输出卷积后的图片O，图片按行输出，行内空格分隔。

第1行输入图片的大小h、w由空格分隔。

第2行到h+1行输入由空格分隔的w个像素值。

第h+2输入卷积核大小m。

第h+3行到h+2+m行输入由空格分隔的m卷积核值

import math
h, w = list(map(int, input().split()))
graph = []
for _ in range(h):
    graph.append(list(map(int, input().split())))
m = int(input())
kernel = []
for _ in range(m):
    kernel.append(list(map(float, input().split())))
result = [[0 for _ in range(w - m + 1)] for _ in range(h - m + 1)]
def cnn(i, j, m):
    result = 0
    for ii in range(m):
        for jj in range(m):
            result += graph[i + ii][j + jj] * kernel[ii][jj]
    return min(math.floor(result), 255)
for i in range(h - m + 1):
    for j in range(w - m + 1):
        result[i][j] = cnn(i, j, m)
for i in range(h - m + 1):
    for j in range(w - m + 1):
        if j != w - m:
            print(result[i][j], end = " ")
        else:
            print(result[i][j])
