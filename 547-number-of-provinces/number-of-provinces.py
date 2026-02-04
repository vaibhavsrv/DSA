from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        pro = 0

        for i in range(n):
            if not visited[i]:
                pro += 1
                q = deque()
                q.append(i)
                visited[i] = True

                while q:
                    curr = q.popleft()
                    for j in range(n):
                        if isConnected[curr][j] == 1 and not visited[j]:
                            visited[j] = True
                            q.append(j)
        return pro