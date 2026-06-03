class Solution:
    def earliestFinishTime(self, LST: List[int], LD: List[int], WST: List[int], WD: List[int]) -> int:
        left = min(a + b for a,b in zip(LST,LD))
        right = min(a + b for a,b in zip(WST,WD))

        return min(min(max(left,a) + b for a,b in zip(WST,WD)),
           min(max(right,a) + b for a,b in zip(LST,LD)))