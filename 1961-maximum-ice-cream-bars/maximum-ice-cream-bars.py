class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_val = max(costs)
        n = len(costs)
        count = [0] * (max_val + 1)

        for num in costs:
            count[num] += 1

        result = []
        for i in range(len(count)):
            result.extend([i]*count[i])

        sum1 = 0
        cnt = 0
        for i in range(len(result)):
            sum1 += result[i]
            if sum1 <= coins:
                cnt += 1

        return cnt

        
