class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        rotate = sum(i * nums[i] for i in range(n))

        answer = rotate

        for k in range(1,n):
            rotate = rotate + total - n * nums[n-k]
            answer = max(answer,rotate)

        return answer