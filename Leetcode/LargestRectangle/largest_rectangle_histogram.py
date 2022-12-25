# 84 - https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack 
        stack = list()
        max_area = 0
        i = 0

        while i < len(heights):                                           
            while stack and (heights[i] < heights[stack[-1]]):
                top_index = stack.pop()
                prev_area = heights[top_index] * ((i - stack[-1] - 1) if stack else i )
                max_area = max(max_area, prev_area)

            stack.append(i)
            i += 1
        
        # emptying the stack
        while stack:
            top_index = stack.pop()
            prev_area = heights[top_index] * ((i - stack[-1] - 1) if stack else i)
            max_area = max(prev_area, max_area)

        return max_area
