from typing import List
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n=len(grid)
        zeros = [0]*n
        for i in range(n):
            for j in range(n-1,-1,-1):
                if grid[i][j] == 0:
                    zeros[i] += 1
                else:
                    break
        swap = 0
        for i in range(n):
            need = n-1-i
            j = i
            while j<n and zeros[j] < need:
                j+=1
            if j == n:
                return -1
            while j>i:
                zeros[j],zeros[j-1] = zeros[j-1], zeros[j]
                swap += 1
                j -= 1
        return swap