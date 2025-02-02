class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(char) for char in digits]
        str_digits = "".join(digits)
        digits = str(int(str_digits) + 1)
        return [int(digit) for digit in digits]
