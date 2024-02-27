class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur, op = 0, '+'
        s += '+'
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in '+-*/':
                if op == '*':
                    stack.append(stack.pop() * cur)
                if op == '/':
                    stack.append(int(stack.pop() / cur))
                if op == '+':
                    stack.append(cur)
                if op == '-':
                    stack.append(-cur)
                cur, op = 0, c
        return sum(stack)