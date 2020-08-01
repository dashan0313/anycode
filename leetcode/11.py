给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxArea(self, height: List[int]) -> int:

        def tj(i,j,hi,hj):
            return (j-i) * min(hi,hj)

        size = len(height)
        #initialized
        i,j = 0,size-1
        hi,hj = height[i],height[j]
        max_area = tj(i,j,hi,hj)
        #
        while i<j:
            if hi<hj:
                i += 1
                hi,hj = height[i],height[j]
                if hi<height[i-1]:
                    continue
                current_area = tj(i,j,hi,hj)
                if current_area > max_area:
                    max_area = current_area

            else:
                j -= 1
                if hi<height[j+1]:
                    continue
                hi,hj = height[i],height[j]
                current_area = tj(i,j,hi,hj)
                if current_area > max_area:
                    max_area = current_area

        return max_area
