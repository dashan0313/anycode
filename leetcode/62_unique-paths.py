def uniquePaths(m,n):
        res = 0
        nums = [0]*m + [1]*n
        length = m+n-2
        visited = [0] * length

        def back(length):
            if length == n:
                res += 1

            for i in range(n):
                if visited[i] or (i>0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                visited[i] = 1
                back(length + 1)
                visited[i] = 0

            print(res)

        back(0)

        return res

uniquePaths(3,2)
