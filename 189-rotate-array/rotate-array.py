class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array to the right by k steps.
        """
        n = len(nums)
        if k == 0:
            pass
        if k > n:
            k = k % n
        if k == k % n:
            nums.reverse()
            nums[0:k] = nums[0:k][::-1] 
            nums[k:] = nums[k:][::-1] 
