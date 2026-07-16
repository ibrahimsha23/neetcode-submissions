class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        n = len(heights)

        low, high = 0, n-1
        max_result = 0

        while low < high:

            width = (high - low)
            water_holding_limit =  min(heights[low], heights[high])
            max_result = max(max_result, water_holding_limit * width)

            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1
        return max_result