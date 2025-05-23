class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        closest = float('inf')
    
        for i in range(len(nums)-2):
            r = len(nums) - 1
            l = i+1
            while l<r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    return curr_sum

        return closest

        

           



        


