class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        count = len(nums)+1

        for i in range(len(nums)):
            curr = 0
            for j in range(i,len(nums)):
                curr |= nums[j]
                
                if curr >= k:
                    count = min(count,j-i+1)

        if count == len(nums)+1:
            return -1

        return count