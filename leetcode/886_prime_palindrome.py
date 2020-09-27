求出大于或等于 N 的最小回文素数。

回顾一下，如果一个数大于 1，且其因数只有 1 和它自身，那么这个数是素数。

例如，2，3，5，7，11 以及 13 是素数。

回顾一下，如果一个数从左往右读与从右往左读是一样的，那么这个数是回文数。

例如，12321 是回文数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/prime-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def primePalindrome(self, N):
        def is_prime(n):
            return n > 1 and all(n%d for d in range(2, int(n**.5) + 1))

        for length in range(1, 6):
            #Check for odd-length palindromes
            for root in range(10**(length - 1), 10**length):
                s = str(root)
                x = int(s + s[-2::-1]) #eg. s = '123' to x = int('12321')
                if x >= N and is_prime(x):
                    return x
                    #If we didn't check for even-length palindromes:
                    #return min(x, 11) if N <= 11 else x

            #Check for even-length palindromes
            for root in xrange(10**(length - 1), 10**length):
                s = str(root)
                x = int(s + s[-1::-1]) #eg. s = '123' to x = int('123321')
                if x >= N and is_prime(x):
                    return x

class Solution(object):
    def primePalindrome(self, N):
        def is_prime(n):
            return n > 1 and all(n % d for d in xrange(2, int(n**.5) + 1))

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x /= 10
            return ans

        while True:
            if N == reverse(N) and is_prime(N):
                return N
            N += 1
            if 10**7 < N < 10**8:
                N = 10**8
