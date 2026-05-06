class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = {}
        for x in range(len(arr)):
            index =  ((arr[x] % k) + k) % k

            freq[index] = freq.get(index,0) + 1

        if freq.get(0,0) % 2 != 0:
            return False
        for i in range(1,k):
            if freq.get(i,0) != freq.get(k-i,0):
                return False

        return True
