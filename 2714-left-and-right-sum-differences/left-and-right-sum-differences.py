class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = 0

        for num in nums:
            total += num

        leftSum = 0
        answer = []

        for num in nums:
            total -= num
            answer.append(abs(leftSum-total))
            leftSum += num

        return answer