def firstPosition(nums, target):

    l = 0
    r = len(nums) - 1
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            res = mid
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return res
def lastPosition(nums, target):

    l = 0
    r = len(nums) - 1
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            res = mid
            l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return res


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [firstPosition(nums,target), lastPosition(nums,target)]
    
        

