class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(c**0.5) + 1

        for a in range(n):
            b = c - a**2
            if int(b**0.5)**2 + a**2 == c:
                return True
        return False

            


        

            