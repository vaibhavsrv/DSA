class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] > k*nums[j]:
                j+=1
        return j