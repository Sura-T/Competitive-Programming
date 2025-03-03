class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = s.count('1')
        count_zero = s.count('0')

        s = ''
        while count_one - 1 != 0:
            s += '1'
            count_one -= 1
        while count_zero != 0:
            s += '0'
            count_zero -= 1
        
        s += '1'
        return s


