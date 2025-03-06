class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[1])
        ans = 0
        last = float('-inf')
        for x_start, x_end in sorted_points:
            if x_start > last:
                ans += 1
                last = x_end

        return ans
     

            


            
