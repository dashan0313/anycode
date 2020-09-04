给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：

区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:



[6] = 6 * 6 = 36;

[2] = 2 * 2 = 4;

[1] = 1 * 1 = 1;

[6,2] = 2 * 8 = 16;

[2,1] = 1 * 3 = 3;

[6, 2, 1] = 1 * 9 = 9;



从上述计算可见选定区间 [6] ，计算值为 36， 则程序输出为 36。

区间内的所有数字都在[0, 100]的范围内;

自己写的30%通过率的垃圾代码
n = int(input())
nums = list(map(int,input().split()))
res = 0

for i in range(n):
    tmp = nums[i]*nums[i]
    if tmp>res:
        res = tmp
    for j in range(n-1,i,-1):
        tmp = min(nums[i:j+1]) * sum(nums[i:j+1])
        if tmp > res:
            res = tmp

print(res)

全通过的牛逼玩意
if __name__ == "__main__":
    n = int(input())
    inlist = list(map(int,input().split()))

    res = 0
    for i in range(n):
        tmp = inlist[i]
        if tmp == 0:
            continue
        l = r = i
        while l - 1 >= 0 and inlist[l - 1] >= tmp:
            l -= 1
        while r + 1 < n and inlist[r + 1] >= tmp:
            r += 1
        res = max(res, tmp * sum(inlist[l:r + 1]))
    print(res)
