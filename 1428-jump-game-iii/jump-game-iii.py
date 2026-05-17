class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        return self.dfs(arr,start)

    def dfs(self,arr,i):
        if i < 0 or i >= len(arr) or arr[i] < 0:
            return False

        if arr[i] == 0:
            return True

        arr[i] *= -1

        left = self.dfs(arr,i+arr[i])
        right = self.dfs(arr,i-arr[i])

        return left or right