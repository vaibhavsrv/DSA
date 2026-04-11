class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        first = [-1] * (n + 1)
        second = [-1] * (n + 1)
        high = n * 2
        result = high

        for index in range(n):
            value = nums[index]

            fir = first[value]
            sec = second[value]

            if fir != -1:
                result = min(result,2 * (index - fir))
            first[value] = sec
            second[value] = index

        return -1 if result == high else result