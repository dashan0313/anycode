编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2,i3,i5 = 0,0,0
        res = [1]

        i = 1

        while i < n:
            ugly = min(2*res[i2],3*res[i3],5*res[i5])
            res.append(ugly)
            if 2*res[i2] == ugly:
                i2+=1
            if 3*res[i3] == ugly:
                i3+=1
            if 5*res[i5] == ugly:
                i5+=1

            i+=1


        return res[-1]
