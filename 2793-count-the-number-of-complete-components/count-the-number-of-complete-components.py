class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        edgeSet = set()

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

            edgeSet.add((min(u,v),max(u,v)))

        visited = [False]  * n
        result = 0

        for start in range(n):
            if visited[start]:
                continue
            stack = [start]
            visited[start] = True

            component = []

            while stack:
                node = stack.pop()
                component.append(node)

                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)       

            isComp = True

            for i in range(len(component)):
                for j in range(i+1,len(component)):
                    u,v = component[i],component[j]

                    if (min(u,v),max(u,v)) not in edgeSet:
                        isComp = False


                if not isComp:
                    break

            if isComp:
                result += 1

        return result