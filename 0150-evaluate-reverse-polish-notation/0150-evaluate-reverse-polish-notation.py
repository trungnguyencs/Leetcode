class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                num2, num1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                if token == '-':
                    stack.append(num1 - num2)
                if token == '*':
                    stack.append(num1 * num2)
                if token == '/':
                    stack.append(int(num1 / num2))
        return stack[0]