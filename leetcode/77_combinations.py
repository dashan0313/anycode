给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))

        answers = []
        def back(start,tmp):
            if len(tmp)==k:
                answers.append(tmp)
                return
            for i in range(start,n):
                back(i+1,tmp+[nums[i]])

        back(0,[])

        return answers
