class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         if not s:
            return 0
        max_len = 1
        i,j=0,1
        n = len(s)
        tmp = s[0]
        print('i,j = ',i,j,'  tmp = ',tmp,end = '\n')
        while j < n:
            if not s[j] in tmp:
                j+=1
            else:
                sj_index = tmp.find(s[j])
                i = i+ sj_index+1
                j+=1
                if i>j:
                    j==i

            tmp = s[i:j]

            print('i,j = ',i,j,'  tmp = ',tmp,end = '\n')
            tmp_len = j-i
            if tmp_len > max_len:
                max_len = tmp_len

        return(max_len)

test = Solution()
test.lengthOfLongestSubstring('abcabcbb')
