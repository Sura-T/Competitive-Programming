class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        n = len(piles)

        rotate = n//3
        i = 0
        cnt = 0
        sum1 = 0
        while cnt < rotate:
            sum1 += piles[i+1] 
            cnt += 1
            i += 2
        
        return sum1
        



