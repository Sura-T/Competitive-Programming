class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
            n = len(prices)
            for i in range(n):
                discount_applied = False
                for j in range(i + 1, n):
                    if prices[j] <= prices[i]:
                        prices[i] -= prices[j]
                        discount_applied = True
                        break
                if not discount_applied:
                    prices[i] = prices[i]
            return prices
        