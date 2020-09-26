给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n<4:
            return(n-1)
        res = [0]*(n+1)
        res[1:4] = [1,2,3]
        for i in range(4,n+1):
            j=1
            while j <= i/2:
                res[i] = max(res[i],res[j]*res[i-j])
                j+=1

        return(res[-1])


class Solution {
public:
    int cuttingRope(int n) {
        if(n <= 3) return n - 1;
        int res = 0, count3 = n / 3;
        if(n % 3 == 0) return pow(3, count3);
        else if( n % 3 == 1)
        {
            count3 --;
            return pow(3, count3) * 4;
        }
        else return pow(3, count3) * 2;
    }
};
