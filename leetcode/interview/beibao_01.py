
def find1array():
    C = 10  # 背包总体积
    num = 5 # 物品个数
    v   =   [4, 3, 5, 2, 5] # 每个物品体积
    price = [9, 6, 1, 4, 1]  # 初始定义好的价格
    dp=[0 for i in range(C+1)] # 定义固定大小()的数组
    for i in range(num): # 从第i个物品开始遍历
        for j in range(C,v[i]-1,-1): # 从容量开始往下递减
            dp[j]=max(dp[j],dp[j-v[i]]+price[i])

    print("一维递归计算结果：",dp[C])
 
