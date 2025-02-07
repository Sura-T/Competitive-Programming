class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        percent = (s.count(letter) / len(s)) * 100

        return floor(percent)