class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        result = []
        visited=set()
        thestack=[0]*n
        def dfs(i):
            if thestack[i] == 1: 
                return True
            if thestack[i] == -1: 
                return False
            if len(graph[i]) == 0:
                thestack[i] = 1
                return True
            thestack[i] = -1
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            thestack[i] = 1
            return True
        for i in range(n):
            if dfs(i):
                result.append(i)       
        return result