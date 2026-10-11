class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sumof = 0
        n = len(nums)
        for i in range(1,n+1):
            square = 1
            if n % i== 0:
                square= nums[i-1]*nums[i-1]
                sumof+= square
        return sumof