class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''m,n = len(matrix),len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True

        return False'''
        m = len(matrix[0])
        for row in matrix:
            if row[0] > target or row[m-1] < target:
                continue

            low,high = 0,m-1

            while low <= high:
                mid = (low + high) // 2

                if row[mid] == target:
                    return True

                elif row[mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1

        return False