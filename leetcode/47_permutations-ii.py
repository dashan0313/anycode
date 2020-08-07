给定一个可包含重复数字的序列，返回所有不重复的全排列。

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        answer = []
        nums.sort()
        n = len(nums)
        visited = [0] * n

        def back(tmp,length):
            if length == n:
                answer.append(tmp)

            for i in range(n):
                if visited[i] or (i>0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                visited[i] = 1
                back(tmp + [nums[i]],length + 1)
                visited[i] = 0

        back([],0)
        return answer
