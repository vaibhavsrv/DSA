class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for i in range(len(graph)):
            if i not in colors:
                queue = [(i,1)]
                colors[i] = 1
                while queue:
                    node,current = queue.pop(0)
                    for nei in graph[node]:
                        if nei in colors:
                            if colors[nei] == current:
                                return False
                        else:
                            colors[nei] = -current
                            queue.append((nei,-current))
        return True