class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        minimumDistance = 0
        for i in range(len(colors)):
            if colors[i] != colors[0]:
                minimumDistance = max(minimumDistance,i)

            if colors[i] != colors[n-1]:
                minimumDistance = max(minimumDistance,n-1-i)
        
        return minimumDistance
