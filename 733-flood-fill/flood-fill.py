class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        initial_color = image[sr][sc]
        if image[sr][sc] == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if image[i][j] != initial_color:
                return

            image[i][j] = color

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        dfs(sr, sc)
        return image