给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        answer = []

        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for ew in range(i+1,size):
                if ew > i+1 and nums[ew] ==nums[ew - 1]:
                    continue
                #第四个指针倒着找，找到第一个就行
                k = size - 1
                check = target - nums[i] - nums[ew]
                for j in range(ew + 1,size):
                    #相同的连续数只取第一个！
                    if j > ew+1 and nums[j] == nums[j-1]:
                        continue
                    #倒着找，要是小于就无了
                    while j < k and nums[j]+nums[k]>check:
                            k -= 1
                    if j == k:
                        break
                    if nums[i] + nums[ew] + nums[j] + nums[k] - target == 0:
                        answer.append([nums[i],nums[ew],nums[j],nums[k]])

        return answer
