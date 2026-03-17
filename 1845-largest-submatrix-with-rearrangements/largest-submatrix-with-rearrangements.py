class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        answer = 0
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        for i in range(m):
            matrix[i].sort(reverse=True)
            for width in range(1,n + 1):
                height = matrix[i][width - 1]
                answer = max(answer,height * width)

        return answer