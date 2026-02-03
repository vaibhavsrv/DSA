class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        indegree = {}
        for u,v in edges:
            indegree[u] = indegree.get(u,0)+1
            indegree[v] = indegree.get(v,0)+1
        center = max(indegree,key=indegree.get)
        return center