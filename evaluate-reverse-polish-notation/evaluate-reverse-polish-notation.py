class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in '+-*/':
                stack.append(int(ch))
            else:
                num2, num1 = stack.pop(), stack.pop()
                if ch == '+': stack.append(num1 + num2)
                elif ch == '-': stack.append(num1 - num2)
                elif ch == '*': stack.append(num1 * num2)
                elif ch == '/': stack.append(int(num1 / num2))
        return stack[-1]      