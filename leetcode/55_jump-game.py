#递归失败，超出时间限制
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 0:
            return False
        if n == 1:
            return True

        left = n-1

        for i in range(0,left):
            if nums[i] + i >= left:
                if i == 0:
                    return True
                else:
                    return self.canJump(nums[0:(i+1)])

        return False


给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= n:
                n = 1
            else:
                n += 1

            if i == 0 and n > 1:
                return False

        return True
