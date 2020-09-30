class Solution:
    def restoreIpAddresses(self, s):
        res = []
        n = len(s)
        if not s:
            return []
        if n==4:
            return([s[0]+'.'+s[1]+'.'+s[2]+'.'+s[3]])
        def check(num_str):
            if num_str =='0':
                return True
            if num_str[0] == '0' or int(num_str) > 255:
                return False
            else:
                return True

        def back(pre_index,index,position,tmp):
            print('preindex,index,position= ',pre_index,index,position)
            print('tmp = ',tmp)
            res_len = n - pre_index
            print('res_len = ',res_len)
            if position == 0:
                for i in range(3):
                    #print(i,pre_index,index+1)
                    current_nums = s[pre_index:index+i+1]
                    print(current_nums)
                    if check(current_nums):
                        back(index,index+i,position+1,tmp)
            else:
                if  (5-position)*3 >= res_len >= (5-position):
                    #print('i m here')
                    current_nums= s[pre_index:index+1]
                    print(current_nums,'------------------')
                    if check(current_nums):

                        if position == 4:
                            tmp = tmp + [current_nums]
                            res.append('.'.join(tmp))
                            return
                        if position == 3:
                            back(index+1,n-1,position+1,tmp+[current_nums])
                        else:
                            for i in range(3):
                                back(index+1,index+i+1,position+1,tmp+[current_nums])
                    else:
                        return False
                else:
                    return False
        back(0,0,0,[])
        return res

mytest = Solution()
print(mytest.restoreIpAddresses('0000'))
