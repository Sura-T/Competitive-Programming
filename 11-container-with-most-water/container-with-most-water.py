class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1

        max_area = 0
        while l < r:
            min_height = min(height[l],height[r])
            width = r - l
            curr_area = min_height * width

            max_area = max(curr_area,max_area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
