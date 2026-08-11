class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set(nums)
        s = nums[0]
        for i in range(1,n):
            if nums[i] == nums[i-1]+1:
                s += nums[i]
            else:
                break

        while s in seen:
            s += 1
        
        return s