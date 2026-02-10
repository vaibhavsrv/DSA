class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        length=0
        for i in range(n):
            evencount = set()
            oddcount = set()
            for j in range(i,n):
                if nums[j]%2==0:
                    evencount.add(nums[j])
                else:
                    oddcount.add(nums[j])
                if len(evencount) == len(oddcount):
                    length = max(length,j-i+1)
        return length