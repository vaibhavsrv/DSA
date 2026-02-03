class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''if len(trust) == 0 and n == 1:
            return 1
        count = [0] * (n+1)
        for i,j in trust:
            count[i] -= 1
            count[j] += 1
        for p,c in enumerate(count):
            if c == n - 1 :
                return p
        return -1'''
        indegree = [0]*(n+1)
        outdegree = [0]*(n+1)

        for a,b in trust:
            indegree[b]+=1
            outdegree[a]+=1
        
        for i in range(1,n+1):
            if indegree[i] == n-1 and outdegree[i]==0:
                return i
        return -1