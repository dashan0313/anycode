给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]
        for i in range(1,n):
            #print(dp)
            for j in range(i,-1,-1):
                if j == i:
                    dp[j] = dp[i-1] + triangle[i][j]
                elif j==0:
                    dp[j] += triangle[i][j]
                else:
                    dp[j] = min(dp[j],dp[j-1]) + triangle[i][j]

        return min(dp)
