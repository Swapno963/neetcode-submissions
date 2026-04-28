class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start from 0 to len -1
        l = 0
        r = len(heights) - 1
        max_area = 0

        for _ in range(len(heights)):
            # Calculate the area
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)

            #  move pointer
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area