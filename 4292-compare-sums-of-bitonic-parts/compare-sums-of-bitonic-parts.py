class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        mid = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[mid]:
                mid = i

        ascending = sum(nums[:mid+1])
        descending = sum(nums[mid:])

        if ascending == descending:
            return - 1
        return 1 if descending > ascending else 0