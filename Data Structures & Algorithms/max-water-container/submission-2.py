class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        n = len(heights)

        for start_idx in range(n - 1):
            print(start_idx)
            for end_idx in range(start_idx+1, n):
                # print(start_idx, end_idx)
                min_ht = min(heights[start_idx], heights[end_idx])
                water_holder = min_ht * (end_idx - start_idx)



                max_water = max(water_holder, max_water)
        return max_water
