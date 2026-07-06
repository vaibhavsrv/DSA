class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[0],-x[1]))

        ans = len(intervals) 

        l = intervals[0][0]
        r = intervals[0][1]

        for i in range(1,len(intervals)):
            if intervals[i][0] == l or intervals[i][1] <= r:
                ans -= 1

            else:
                l = intervals[i][0]
                r = intervals[i][1]

        return ans
