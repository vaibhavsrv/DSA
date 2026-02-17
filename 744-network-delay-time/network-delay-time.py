import math
import heapq
from collections import defaultdict
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u,v,w in times:
            g[u].append((v,w))
        dist = [math.inf]*(n+1)
        dist[k] = 0
        pq = [(0,k)]
        while pq:
            d,u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v,w in g[u]:
                if dist[u]+w < dist[v]:
                    dist[v] = dist[u]+w
                    heapq.heappush(pq,(dist[v],v))
        ans = max(dist[1:])
        return -1 if ans == math.inf else ans