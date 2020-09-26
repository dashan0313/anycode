n = int(input())

nums = []
for i in range(n):
    tmp = list(map(int,list(input().strip(' ').split(' '))))
    nums.append(tmp)

def dt(c,pos,tmp):
    if c == n-1:
        return max(tmp+nums[c][pos],tmp+nums[c][pos+1],tmp+nums[c][pos+2])
    return max(dt(c+1,pos,tmp+nums[c][pos]),dt(c+1,pos+1,tmp+nums[c][pos+1]),dt(c+1,pos+2,tmp+nums[c][pos+2]))

dt(0,0,0)
