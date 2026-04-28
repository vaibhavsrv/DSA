class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = [0]

        for i in gain:
            a = sum[len(sum) - 1]
            b = i + a

            sum.append(b)
        return max(sum)