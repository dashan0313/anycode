给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 如果数组为空
        if not nums:
            return [-1,-1]
        # 定义初始边界
        low, high = 0, len(nums) - 1
        left = -1
        right = len(nums) - 1
        # 先找左边
        while low <= high:
            mid = (low + high) >> 1
            # 如果此时的索引对应的值为target，如果是那么有种情况说明这是左边界：1.mid==0时，即数组的最左边。2.当前值左面的值不是目标值
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                left = mid
                break
            # 正常二分操作
            if nums[mid] < target:
                low = mid + 1
            else:
            # 注意一下这个 else 的操作包括了两种含义：1.nums[mid] > target。2. nums[mid] == target and nums[mid-1] != target 时需要左移
                high = mid - 1
        # 不存在目标值
        if left == -1:
            return [-1, -1]
        # 重新定义区间
        high = len(nums) - 1
        # 此时的左区间就从target的最左区间开始就可以了，没必要从0开始
        low = left
        while low <= high:
            mid = (low + high) >> 1
            # 如果此时的索引对应的值为target，如果是那么有种情况说明这是左边界：1.mid==len(nums)-1时，即数组的最左边。2.当前值左面的值不是目标值
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target):
                right = mid
                break

            if nums[mid] > target:
                high = mid - 1
            else:
            # 注意一下这个 else 的操作包括了两种含义：1.nums[mid] < target。2. nums[mid] == target and nums[mid+1] != target 时需要右移
                low =  mid + 1

        return [left,right]

作者：xiao-xue-66
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/pythonti-jie-liang-ci-er-fen-cha-zhao-by-xiao-xue-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
