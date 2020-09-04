给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        length = len(A)
        j = 0
        for i in range(length):
            if A[i]%2 == 0:
                A[i],A[j] = A[j],A[i]
                j += 1
        return A
