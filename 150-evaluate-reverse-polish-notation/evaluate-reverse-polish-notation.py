class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-*/'
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                val = 0
                if token == '+':
                    val += stack[-1] + stack[-2]
                elif token == '-':
                    val += stack[-2] - stack[-1]
                elif token == '*':
                    val += stack[-1] * stack[-2]
                else:
                    val += int(stack[-2] / stack[-1])

            
                stack.pop()
                stack.pop()
                stack.append(val)

        return stack[-1]





        