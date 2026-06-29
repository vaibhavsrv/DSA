class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newNums = set(nums)

        best = 1

        if not nums:
            return 0

        for num in newNums:
            if num -1 not in newNums:
                curr = num
                length = 1

                while curr + 1 in newNums:
                    curr += 1
                    length += 1

                best = max(best, length)

        return best