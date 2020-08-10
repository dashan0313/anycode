给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = ''
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if int(str(nums[i])+str(nums[j])) < int(str(nums[j])+str(nums[i])):
                    nums[i],nums[j] = nums[j],nums[i]
        for x in (nums):
            s += str(x)
        return str(int(s))


#官方题解
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

作者：LeetCode
链接：https://leetcode-cn.com/problems/largest-number/solution/zui-da-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
