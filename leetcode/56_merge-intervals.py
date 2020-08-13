给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#关注merge的最后一个元素对

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        n = len(intervals)
        merge = [intervals[0]]
        for i in range(1,n):
            if intervals[i][0] > merge[-1][1]:
                merge.append(intervals[i])
            else:
                merge[-1][1] = max(merge[-1][1],intervals[i][1])

        return merge
