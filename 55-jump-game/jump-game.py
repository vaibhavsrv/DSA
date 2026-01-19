class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True
        max_index=0
        for i in range(len(nums)):
            if max_index<i:
                return False
            max_index=max(max_index,i+nums[i])
        return True