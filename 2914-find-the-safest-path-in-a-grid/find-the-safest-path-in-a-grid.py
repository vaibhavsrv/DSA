class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        #BSF TO REACH FROM (0,0) T0 (N-1)(N-1)
        n = len(grid)
        dist = [[-1]* n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dist[r][c] = 0
                    q.append((r,c))

        directions = [(0,1),(-1,0),(1,0),(0,-1)]

        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                nx,ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))


        #BFS TO FIND THE MINIMUM DIST

        def solve(x):
            if dist[0][0] < x:
                return False

            q = deque([(0,0)])
            vis = [[0] * (n) for _ in range(n)]
            vis[0][0] = 1

            while q:
                i,j = q.popleft()
                if i == n-1 and j== n-1:
                    return True

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if (0 <= ni < n and 0 <= nj < n and
                        not vis[ni][nj] and dist[ni][nj] >= x):
                        vis[ni][nj] = 1
                        q.append((ni,nj))

            return False

        #binary search for the best ans
        l,r = 0, max(max(row) for row in dist)
        ans = 0

        while l <= r:
            m = (l + r) // 2

            if solve(m):
                ans=m
                l = m+1
            else:
                r = m - 1

        return ans