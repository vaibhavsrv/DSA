from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u) 
        
        visited = [0] * numCourses
        
        def has_cycle(node: int) -> bool:
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False
            visited[node] = 1
            for neighbor in adj[node]:
                if has_cycle(neighbor):
                    return True
            visited[node] = 2
            return False
        
        for i in range(numCourses):
            if visited[i] == 0 and has_cycle(i):
                return False
        return True