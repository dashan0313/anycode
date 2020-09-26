n = int(input())
n_prev = 0
nums = list(map(int,list(input().split(' '))))
count = -1

while n_prev != n and n>1:
    count += 1
    right = n - 1
    res = []
    while right>0:
        if nums[right-1]>nums[right]:
            flag = 0
            right-=1
        else:
            flag = 1
            res.insert(0,right)
            right -= 1
    if (nums[0]>nums[1] and flag == 0) or flag == 1:
        res.insert(0,0)
    new = [nums[k] for k in res]
    nums = new
    print(nums)
    n_prev,n = n,len(nums)

print(count,end='')
