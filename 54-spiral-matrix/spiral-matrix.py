class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])

        initial_i = 0
        last_i = m-1
        initial_j = 0
        last_j = n-1

        answer = []

        while initial_i <= last_i and initial_j <= last_j:
            # top-left to top-right
            for k in range(initial_j,last_j+1):
                answer.append(matrix[initial_i][k])
            initial_i += 1

            #top-right to bottom-right
            for k in range(initial_i,last_i+1):
                answer.append(matrix[k][last_j])
            last_j -= 1

            #bottom right to bottom-left
            if initial_i <= last_i:
                for k in range(last_j,initial_j-1,-1):
                    answer.append(matrix[last_i][k])
                last_i -= 1

            #bottom-left to top-left
            if initial_j <= last_j:
                for k in range(last_i,initial_i-1,-1):
                    answer.append(matrix[k][initial_j])
                initial_j += 1

        return answer