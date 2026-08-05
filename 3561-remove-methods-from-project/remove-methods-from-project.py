class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(n)}

        for src, des in invocations:
            adj[src].append(des)

        q=[k]
        visited = set([k])

        while q:
            sus = q.pop()

            for nei in adj[sus]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        res = []

        for method in range(n):
            if method in visited:
                continue

            for nei in adj[method]:
                if nei in visited:
                    return list(range(n))
            res.append(method)

        return res