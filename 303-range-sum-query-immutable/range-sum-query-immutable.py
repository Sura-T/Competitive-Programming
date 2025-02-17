class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.arr[i] =self.arr[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.arr[right] - self.arr[left-1]
        else:
            return self.arr[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)