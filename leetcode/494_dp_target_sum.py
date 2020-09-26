class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P,num-1,-1):dp[j] += dp[j - num]
        return dp[P]

作者：qsctech-sange
链接：https://leetcode-cn.com/problems/target-sum/solution/python-dfs-xiang-jie-by-jimmy00745/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nsum = sum(nums)
        target = S+nsum
        if target % 2 == 1 or S>nsum: return 0

        target // 2
        res = [0]*(target+1)

        res[0] = 1

        for num in nums:
            i = target
            while i >= num:
                res[i] += res[i-num]
                i-=1


        return(res)
