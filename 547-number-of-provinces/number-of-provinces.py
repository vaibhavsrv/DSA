class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        rank = [0]*n
        def find(x):
            if parent[x] != x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            rankX = find(x)
            rankY = find(y)
            if rankX == rankY:
                return
            if rank[rankX] < rank[rankY]:
                parent[rankX] = rankY
            elif rank[rankX] > rank[rankY]:
                parent[rankY] = rankX
            else:
                parent[rankY] = rankX
                rank[rankX] += 1
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    union(i,j)
        roots = set(find(i) for i in range(n))
        return len(roots)