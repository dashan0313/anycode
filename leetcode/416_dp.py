给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        full_sum = sum(nums)

        if n < 2 or full_sum % 2 == 1:
            return False
        hsum = full_sum // 2

        dp = [False for _ in range(hsum+1)]
        #dp[0] = True
        if nums[0]<=hsum:
            dp[nums[0]] = True
        for i in range(1,n):
            for j in range(hsum,nums[i]-1,-1):
                if dp[hsum]: return True
                dp[j] = dp[j] | dp[j - nums[i]]

        return(dp[hsum])
