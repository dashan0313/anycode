n = input()
n = int(n)
res = []
if n == 1:
    print()
else:
    for i in range(n):
        nums = list(map(int,list(input().split(' '))))
        op = nums[0]
        if op == 1:
            res.insert(nums[1]-1,nums[2])
        elif op == 2:
            res.pop(nums[1]-1)
        elif op == 3 and i != n-1:
            print(' '.join(map(str,res)),end = '\n')
        else:
            print(' '.join(map(str,res)),end = '')
