''' #This is the brute force solution where it takes O(Q*N) -> order of Q times N #
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
    def sumRange(self, left: int, right: int) -> int:
        count = 0
        for i in range(left,right+1):
            count += self.nums[i]
        return count'''
# The optimal can be like->
   # we can pre compute the value of the array and whenever required just return the value
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * len(nums)
        self.prefix[0] = nums[0]
        for i in range(1,len(nums)):
            self.prefix[i] = self.prefix[i-1]+nums[i]
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]             
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)