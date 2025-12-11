class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        for i in range(1,m):
            for j in range(n):
                left = matrix[i-1][j-1] if 0<=j-1 else float('inf')
                down = matrix[i-1][j]
                right = matrix[i-1][j+1] if j+1<n else float('inf')

                matrix[i][j] += min(left,down,right)

        return min(matrix[m-1])