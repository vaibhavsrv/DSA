# BRUTE FORCE SOLUTION WITH O(ROWS*COLS)
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        count = 0
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                count += self.matrix[i][j]
        return count
    
    # GOT *****TLE*****
        # NOW THE OPTIMAL CAN BE LIKE THIS
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        r=len(matrix)
        c=len(matrix[0])
        self.prefix = [[0] *(c) for _ in range(r)]
        for i in range(r):
            for j in range(c):
                self.prefix[i][j] = matrix[i][j]
                if i > 0:
                    self.prefix[i][j] += self.prefix[i-1][j]
                if j > 0:
                    self.prefix[i][j] += self.prefix[i][j-1]
                if i > 0 and j > 0:
                    self.prefix[i][j] -= self.prefix[i-1][j-1]

    def sumRegion(self,row1,col1,row2,col2):
        result=self.prefix[row2][col2]
        if row1>0:
            result-=self.prefix[row1-1][col2]
        if col1>0:
            result-=self.prefix[row2][col1-1]
        if row1>0 and col1>0:
            result+=self.prefix[row1-1][col1-1]
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)