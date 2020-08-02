实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

判断按照字典序有木有下一个，如果完全降序就没有下一个
如何判断有木有下一个呢？只要存在a[i-1] < a[i]的升序结构，就有，而且我们应该从右往左找，一旦找到，因为这样才是真正下一个
当发现a[i-1] < a[i]的结构时，从在[i, ∞]中找到最接近a[i-1]并且又大于a[i-1]的数字，由于降序，从右往左遍历即可得到k
然后交换a[i-1]与a[k]，然后对[i, ∞]排序即可，排序只需要首尾不停交换即可，因为已经是降序 上面说的很抽象，还是需要拿一些例子思考才行，比如[0,5,4,3,2,1]，下一个是[1,0,2,3,4,5]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 找有没有升序结构
        i = len(nums) - 1
        if i == 0:
            return

        flag = 0

        while i > 0 :
            if nums[i-1] < nums[i] :
                flag = 1
                k = len(nums) - 1
                while k >= i :
                    if nums[k] > nums[i-1] :
                        nums[k],nums[i-1] = nums[i-1],nums[k]
                        break
                    else:
                        k -= 1

                nums[i:] = sorted(nums[i:])

                return
            else:
                i -= 1

        if flag == 0:
            nums.sort()
            return

        return
