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
                    continue #1.用过的元素不能再用 2.当前元素和前一个元素相同，并且前一个元素还没有被使用过的时候
                visited[i] = 1 #当前节点访问完了，标记一下
                back(tmp + [nums[i]],length + 1) #进行展开
                visited[i] = 0 #换同层次的下一个节点

        back([],0)
        return answer
