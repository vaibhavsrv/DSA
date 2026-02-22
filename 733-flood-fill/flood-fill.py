class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        def solve(x,y):
            if x < 0 or x >= len(image): return
            if y < 0 or y >= len(image[0]): return 

            if image[x][y] == color: return
            if image[x][y] != start: return
            image[x][y] = color
            solve(x+1,y)
            solve(x,y+1)
            solve(x,y-1)
            solve(x-1,y)
        solve(sr,sc)
        return image