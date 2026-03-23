class Solution:
    def uniformArray(self, a: list[int]) -> bool:
        oddCount = 0
        evenCount = 0
        minimum = a[0] 
        for i in a:
            minimum = min(minimum,i)
            if i % 2:
                oddCount += 1
            else:
                evenCount += 1
        if oddCount == len(a) or evenCount == len(a):
            return True
        if minimum % 2:
            return True
        return False