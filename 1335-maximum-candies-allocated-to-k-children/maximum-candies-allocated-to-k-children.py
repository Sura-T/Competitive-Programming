class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canDistribute(x: int) -> bool:
            total_piles = sum(candy // x for candy in candies)
            return total_piles >= k

        left, right = 1, sum(candies) // k
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if canDistribute(mid):
                answer = mid  
                left = mid + 1
            else:
                right = mid - 1

        return answer
