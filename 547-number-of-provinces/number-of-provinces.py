class UnionFind(object):
    def __init__ (self,n):
        self.u = list(range(n))
    def union(self,a,b):
        ra,rb = self.find(a),self.find(b)
        if ra != rb:
            self.u[ra] = rb
    def find(self,a):
        while self.u[a] != a:
            a=self.u[a]
        return a
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected: return 0
        s=len(isConnected)

        unionfind = UnionFind(s)
        for r in range(s):
            for c in range(r,s):
                if isConnected[r][c] == 1:
                    unionfind.union(r,c)
        return len(set([unionfind.find(i) for i in range(s)]))