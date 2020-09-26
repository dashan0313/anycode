给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#涉及到访问一次就不访问的，用visited
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)
        visited = [0] * n

        if not nums:
            return

        def back(tmp,length):
            if length == n:
                answer.append(tmp)
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = 1
                back(tmp + [nums[i]],length + 1)
                visited[i] = 0

        back([],0)
        return answer
