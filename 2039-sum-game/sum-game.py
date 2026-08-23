class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left = 0
        right = 0
        left_q = 0
        right_q = 0

        for i in range(n//2):
            if num[i] == '?':
                left_q += 1
            else:
                left += int(num[i])

        for i in range(n//2,n):
            if num[i] == '?':
                right_q += 1
            else:
                right += int(num[i])

        if left_q == right_q:
            return left != right

        diff = left - right
        q_d = left_q - right_q

        return diff * 2 + q_d * 9 != 0
        