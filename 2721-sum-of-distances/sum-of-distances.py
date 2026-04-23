class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        map = defaultdict(list)
        for i , num in enumerate(nums):
            map[num].append(i)

        result = [0] * len(nums)

        for value in map:
            array = map[value]
            n = len(array)

            prefix = [0] * n
            prefix[0] = array[0]

            for i in range(1,n):
                prefix[i] = prefix[i-1] + array[i]

            for i in range(n):
                index = array[i]

                leftCount = i
                leftSum = prefix[i-1] if i > 0 else 0
                left = index * leftCount - leftSum

                rightCount = n - i - 1
                rightSum = prefix[n-1] - prefix[i]
                right = rightSum - index * rightCount

                result[index] = left + right
        return result