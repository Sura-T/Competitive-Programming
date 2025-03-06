class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            if stack and logs[i] == '../':
                stack.pop()
            elif logs[i] == './':
                continue
            else:
                stack.append(logs[i])
        
        cnt = 0
        for char in stack:
            if char != '../':
                cnt += 1

        return cnt
