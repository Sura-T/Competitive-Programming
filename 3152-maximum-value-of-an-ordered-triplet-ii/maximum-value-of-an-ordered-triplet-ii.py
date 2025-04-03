class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        # Precompute the maximum (nums[i] - nums[j]) for each j (i < j)
        max_diff = [0] * n
        max_so_far = nums[0]
        for j in range(1, n):
            max_diff[j] = max_so_far - nums[j]
            if nums[j] > max_so_far:
                max_so_far = nums[j]
        
        # Precompute the maximum nums[k] for each j (k > j)
        max_right = [0] * n
        max_so_far = nums[-1]
        for j in range(n - 2, -1, -1):
            max_right[j] = max_so_far
            if nums[j] > max_so_far:
                max_so_far = nums[j]
        
        # Calculate the maximum triplet value
        max_val = 0
        for j in range(1, n - 1):
            current = max_diff[j] * max_right[j]
            if current > max_val:
                max_val = current
        
        return max_val if max_val > 0 else 0