作为一个手串艺人，有金主向你订购了一条包含n个杂色串珠的手串——每个串珠要么无色，
要么涂了若干种颜色。为了使手串的色彩看起来不那么单调，金主要求，
手串上的任意一种颜色（不包含无色），
在任意连续的m个串珠里至多出现一次（注意这里手串是一个环形）。
手串上的颜色一共有c种。现在按顺时针序告诉你n个串珠的手串上，
每个串珠用所包含的颜色分别有哪些。请你判断该手串上有多少种颜色不符合要求。
即询问有多少种颜色在任意连续m个串珠中出现了至少两次。

全部通过

nmc = list(map(int,list(input().split())))
n,m,c = (nmc)
chuan = []
yanse = [0]*c
notok = [0]*c
for _ in range(n):
    zhu = list(map(int,list(input().split())))
    chuan.append(zhu)

for i in range(m):
    zhu = chuan[i]
    for color in zhu[1:]:
        yanse[color-1] += 1

for i in range(c):
    if yanse[i]>1:
        notok[i] = 1

left,right = 0,m-1
while left != n:
    zhu = chuan[left]
    for color in zhu[1:]:
        yanse[color-1] -= 1
    left += 1
    right = (right + 1)%n
    zhu = chuan[right]
    for color in zhu[1:]:
        yanse[color-1] += 1
    for i in range(c):
        if yanse[i]>1:
            notok[i] = 1

print(sum(notok),end = '')
