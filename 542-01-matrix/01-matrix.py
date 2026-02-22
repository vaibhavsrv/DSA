from collections import deque
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols = len(mat),len(mat[0])
        q = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = "*"
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                row = r + dr
                col = c + dc
                if 0 <= row < rows and 0 <= col < cols and mat[row][col] == "*":
                    mat[row][col] = mat[r][c] + 1
                    q.append((row,col))
        return mat