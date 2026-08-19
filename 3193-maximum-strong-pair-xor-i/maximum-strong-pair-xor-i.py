class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maxx = 0

        for x in range(len(nums)):
            for y in range(x,len(nums)):
                a = nums[x]
                b = nums[y]

                if abs(a-b) <= min(a,b):
                    maxx = max(maxx,a^b)
        return maxx