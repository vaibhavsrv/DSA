from collections import deque
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n+1)]

        for u,v, weight in roads:
            graph[u].append((v,weight))
            graph[v].append((u,weight))

        visited = [False] * (n+1)

        q = deque([1])
        visited[1] = True

        ans = float('inf')

        while q:
            u = q.popleft()

            for v,w in graph[u]:
                ans = min(ans, w)

                if not visited[v]:
                    visited[v] = True
                    q.append(v)

        return ans