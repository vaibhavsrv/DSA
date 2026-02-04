from collections import deque,defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        a = defaultdict(list)
        q = deque([source])
        visited = {source}
        for i,j in edges:
           a[i].append(j)
           a[j].append(i)

        while q:
            curr = q.popleft()
            if curr == destination:
                return True
            for x in a[curr]:
                if x not in visited:
                    visited.add(x)
                    q.append(x)
        return False