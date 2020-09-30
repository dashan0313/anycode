在哔哩哔哩相关推荐场景下，用户在某个视频下点击相关推荐视频会产生一条（from_avid, to_avid）的日志记录，
某个用户在某天产生了n条相关推荐点击记录，且每个点击视频的来源视频都唯一，视频可以没来源视频。
可以把用户的浏览记录当作多棵多叉树树遍历的过程，点击树的根节点下面的节点都算由该视频产生的点击，
现在需挖掘产生最多用户点击的视频。

import sys
n = int(sys.stdin.readline().strip("\n"))
tree = {}
maxadv = 0
maxcnt = 0
for i in range(n):
    from_avid,to_avid = map(int,sys.stdin.readline().strip("\n").split(" "))
    tree[to_avid] = from_avid
cnt = {}
for i in tree:
    cnt[i] = cnt.get(i,0)+1
    f = tree[i]
    while f!=0:
        cnt[f] = cnt.get(f,0)+1
        f = tree.get(f,0)
for i in cnt:
    if maxcnt<=cnt[i]:
        maxadv = i if maxcnt < cnt[i] else max(maxadv,i)
        maxcnt = cnt[i]
print(maxadv)

思路很简单，因为父节点唯一，可以建立父节点后，更新的时候每次更新所有父节点，最后对比一下大小即可
