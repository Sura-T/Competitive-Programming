class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = 0
        dq = deque([(-1, 0)])
        min_length = float('inf')

        for i in range(n):
            prefix_sum += nums[i]

            while dq and prefix_sum - dq[0][1] >= k:
                min_length = min(min_length, i - dq.popleft()[0])

            while dq and dq[-1][1] >= prefix_sum:
                dq.pop()

            dq.append((i, prefix_sum))
    
        return min_length if min_length != float('inf') else -1