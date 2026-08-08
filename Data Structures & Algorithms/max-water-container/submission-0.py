class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left, right = 0, len(heights) - 1

        while left < right:
            if heights[left] < heights[right]:
                width = right - left
                max_water = max(max_water, width * heights[left])
                left += 1
            else:
                width = right - left
                max_water = max(max_water, width * heights[right])
                right -= 1

        return max_water