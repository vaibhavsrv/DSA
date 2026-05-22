class Solution:
    def search(self, nums: List[int], target: int) -> int:
        newArr = nums + nums
        for i in range(len(newArr)-1):
            if newArr[i] == target:
                return i

        return -1