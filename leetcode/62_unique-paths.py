def uniquePaths(m,n):
        res = 0
        nums = [0]*m + [1]*n
        length = m+n-2
        visited = [0] * length

        def back(length):
            if length == n:
                res += 1

            for i in range(n):
                if visited[i] or (i>0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                visited[i] = 1
                back(length + 1)
                visited[i] = 0

            print(res)

        back(0)

        return res

uniquePaths(3,2)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        #print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

作者：powcai
链接：https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
