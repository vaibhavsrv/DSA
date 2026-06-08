class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        e = []
        g = []

        for i in nums:
            if i == pivot:
                e.append(i)

            elif i > pivot:
                g.append(i)

            else:
                l.append(i)

        return l + e + g
