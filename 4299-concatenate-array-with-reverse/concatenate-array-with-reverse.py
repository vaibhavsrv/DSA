class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        '''reverse = list(reversed(nums))
        hello = nums + reverse

        return hello'''

        hello = nums + nums[::-1]        
        return hello