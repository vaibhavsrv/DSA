class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c_sum = 0
        overall = -inf

        for num in nums:
            c_sum = max(c_sum+num,num)
            overall = max(overall,c_sum)

        return overall