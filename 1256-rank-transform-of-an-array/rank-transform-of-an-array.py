class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new = sorted(arr)
        map = {}
        r = 1

        for i in new:
            if i not in map:
                map[i] = r
                r +=1

        for i in range(len(arr)):
            arr[i] = map[arr[i]]

        return arr
