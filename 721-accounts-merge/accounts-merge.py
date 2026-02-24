class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n
    def find(self,x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self,x,y):
        a, b = self.find(x),self.find(y)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a,b = b,a
        self.parents[b] = a
        self.size[a] += self.size[b]
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        helper = UnionFind(len(accounts))
        email_to_name = {}
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_name:
                    email_to_name[email] = i
                else:
                    helper.union(i,email_to_name[email])
        components = defaultdict(set)
        for email in email_to_name.keys():
            components[helper.find(email_to_name[email])].add(email)
        answer = []
        for i , j in components.items():
            answer.append([accounts[i][0]] + sorted(j))
        return answer