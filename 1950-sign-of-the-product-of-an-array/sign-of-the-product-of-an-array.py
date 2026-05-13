class Solution:
    def arraySign(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        product = 1

        for i in range(len(nums)):
            product *= nums[i]

        
        if product < 0:
            return -1

        elif product > 0:
            return 1

        else:
            return 0