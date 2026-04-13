class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minimum = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                minimum = min(minimum,abs(i-start))
        return minimum