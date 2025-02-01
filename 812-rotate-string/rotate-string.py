class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = [char for char in s]
        goal = [char for char in goal]

        for _ in range(len(s)):
            if s == goal:
                return True
            else:
                s.append(s[0])
                s.remove(s[0])
        return False
                