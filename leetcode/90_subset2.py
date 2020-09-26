给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        visited = [False] * n

        def helper(i,tmp):
            res.append(tmp)
            for j in range(i,n):
                if j>i and nums[j-1] == nums[j] and not visited[j]:
                    continue
                else:
                    visited[j] = True
                    helper(j+1,tmp+[nums[j]])
                    visited[j] = False

        helper(0,[])
        return res
