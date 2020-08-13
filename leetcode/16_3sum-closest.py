给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10000

        for i in range(0,n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                #总是先找到新的一对可比较的j，k
                current_sum = nums[i]+nums[j]+nums[k]
                if current_sum == target:
                    return target

                if abs(current_sum - target) < abs(best - target):
                    best = current_sum

                if current_sum > target:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return best
