from heapq import heappush, heappop
from math import inf
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid),len(grid[0])
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        heap = [(grid[0][0],0,0)]
        directions =[(1,0),(-1,0),(0,1),(0,-1)]
        while heap:
            cost,x,y = heappop(heap)
            if cost > dist[x][y]:
                continue

            if (x, y) == (m - 1, n - 1):
                return True

            for dx,dy in directions:
                nx, ny = x + dx,y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]
                    if new_cost < dist[nx][ny] and new_cost < health:
                        dist[nx][ny] = new_cost
                        heappush(heap, (new_cost,nx,ny))
        return False