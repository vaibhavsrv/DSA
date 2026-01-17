class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        maximum = 0
        for i in range(n):
            ai,bi = bottomLeft[i]
            ci,di = topRight[i]
            for j in range(i+1,n):
                aj,bj = bottomLeft[j]
                cj,dj = topRight[j]

                height = min(cj,ci)-max(aj,ai)
                width = min(dj,di)-max(bj,bi)

                maximum = max(maximum,min(height,width))
        return maximum*maximum