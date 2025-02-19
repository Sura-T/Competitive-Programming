class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        move = [0] * len(s)
        for start, end, dir in shifts:
            sign = 1 if dir else -1
            move[start] += sign
            if end+1 < len(move):
                move[end+1] -= sign
        
        r = 0
        res = ''
        for i in range(len(move)):
            r += move[i]
            o = (ord(s[i]) + r - ord('a')) % 26 + ord('a')
            res += chr(o)
        return ''.join(res)