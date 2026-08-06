class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for i in sorted(arr,key=abs):
            if count[i] == 0:
                continue
            if count[2*i] == 0:
                return False

            count[i] -=1
            count[2*i] -=1

        return True