判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n= len(x)
        for i in range(n//2):
            if x[i] != x[n -1 - i]:
                return False

        return True
