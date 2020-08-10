一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid),len(obstacleGrid[0])
        f = [0]*n
        f[0] = int(obstacleGrid[0][0] == 0);
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[j] = 0
                    continue
                if j - 1 >= 0 and obstacleGrid[i][j - 1] == 0:
                    f[j] += f[j - 1]

        return f[-1]
