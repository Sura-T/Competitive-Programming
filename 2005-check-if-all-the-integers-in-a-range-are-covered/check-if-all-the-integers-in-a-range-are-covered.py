class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff_arr = [0] * 52

        for start,end in ranges:
            diff_arr[start] += 1
            diff_arr[end + 1] -= 1
        
        coverage = [0] * 52
        for i in range(1,52):
            coverage[i] = coverage[i-1] + diff_arr[i]
        
        for x in range(left,right+1):
            if coverage[x] <= 0:
                return False
                
        return True
