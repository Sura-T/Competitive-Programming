class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if stack and s[i] == '*':
                stack.pop()
            else:
                stack.append(s[i])

        res = "".join(stack)
        return res