class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        pq = [(0,0,0)]
        visited = set()
        visited.add((0,0))
        while pq:
            cost,d,u = heapq.heappop(pq)
            if d == rows-1 and u == cols-1:
                return cost
            for dr,dc in directions:
                if min(d+dr,u+dc)<0 or d + dr == rows or u+dc == cols or (d+dr,u+dc) in visited:
                    continue
                visited.add((d+dr,u+dc))
                if grid[d+dr][u+dc] == 1:
                    heapq.heappush(pq,(cost+1,d+dr,u+dc))
                else:
                    heapq.heappush(pq,(cost,d+dr,u+dc))
