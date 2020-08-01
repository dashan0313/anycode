给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#这个方法很慢
#要注意的就是避开重复数据

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        answer = []

        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #第三个指针倒着找，找到第一个就行
            k = size - 1
            target = - nums[i]
            for j in range(i+1,size):
                #相同的连续数只取第一个！
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                #倒着找，要是小于就无了
                while j < k and nums[j]+nums[k]>target:
                        k -= 1
                if j == k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    answer.append([nums[i],nums[j],nums[k]])

        return answer
