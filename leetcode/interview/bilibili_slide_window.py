
你跟小伙伴一起去参加漫展，逛了一天之后你们准备买点手办回家。现在你们来到一排展台前，每个展台有卖不同的手办。
但是当天售卖有一个特别的规矩：首先每个展台只有一个手办可买，并且只能买连续相邻某几个展台的手办。
现在你跟小伙伴先从头到尾浏览了一遍，知道了总共N家展台，每家展台的手办价格P[0]～P[N-1]，小伙伴说愿意资助你S块钱，多的你自付。
所以你决定至少要花掉S。但是逛了一天也挺累了，所以你希望能在尽量少的展台花掉小伙伴资助的S，然后回家。

输入第一行是两个整数，分别代表展台的数量N，和小伙伴愿意资助的S；

输入第二行是N个整数，分别代表依次N个展台手办的价格；

你需要考虑的是如果至少要花掉S块（包含S），你最少可以只逛几个展台；当然如果小伙伴是土豪，所有展台手办买一遍还是花不完S，那么返回-1让我们羡慕一下

n,s = map(int,input().split(' '))
num = list(map(int,input().split(' ')))
left = 0
right = 0
temp = 0
length = n+1
while right < n:
    if temp < s:
        temp += num[right]
        right += 1
    else:
        length =min(length,right-left)  #因为上面的right + 1了所以这里直接减
        temp -= num[left]
        left += 1
while temp >= s:
    length = min(length,n-left)
    temp -= num[left]
    left += 1
if length == n+1:
    print('-1')
else:
    print(length)
