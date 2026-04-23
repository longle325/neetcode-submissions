class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0 
        while True: 
            if left >= right: break
            current_area = min(heights[left], heights[right]) * (right-left)
            if current_area > max_area: max_area = current_area
            if heights[left] >= heights[right]: 
                right -=1 
            elif heights[left] < heights[right]:
                left += 1

        return max_area