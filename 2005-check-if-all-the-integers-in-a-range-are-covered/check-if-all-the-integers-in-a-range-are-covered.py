class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        #Initialize the difference array with 52 elements 1 extra space
        diff_arr = [0] * 52

        #Iterate over the range in the ranges
        for start,end in ranges:
            diff_arr[start] += 1
            diff_arr[end + 1] -= 1
        
        #Calculate the prefix sum to get the coverage
        coverage = [0] * 52
        for i in range(1,52):
            coverage[i] = coverage[i-1] + diff_arr[i]
        
        #Check if all integers in the range [left, right] covered
        for x in range(left,right+1):
            if coverage[x] <= 0:
                return False
                
        return True
