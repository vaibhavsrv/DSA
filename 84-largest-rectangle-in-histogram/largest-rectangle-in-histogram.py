class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                j = stack.pop()

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, heights[j] * width)

            stack.append(i)

        n = len(heights)

        while stack:
            j = stack.pop()

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n

            max_area = max(max_area, heights[j] * width)

        return max_area