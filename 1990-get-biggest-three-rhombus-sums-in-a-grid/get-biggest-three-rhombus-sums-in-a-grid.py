class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        res = set()

        for i in range(m):
            for j in range(n):
                res.add(grid[i][j])

                k = 1
                while i-k >= 0 and i+k < m and j-k >= 0 and j+k < n:
                    total = 0

                    x,y = i-k,j
                    for t in range(k):
                        total += grid[x+t][y+t]
                    x,y = i,j+k
                    for t in range(k):
                        total += grid[x+t][y-t]
                    x,y = i+k,j
                    for t in range(k):
                        total += grid[x-t][y-t]
                    x,y = i,j-k
                    for t in range(k):
                        total += grid[x-t][y+t]
                    res.add(total)
                    k += 1
        return sorted(res, reverse=True)[:3]