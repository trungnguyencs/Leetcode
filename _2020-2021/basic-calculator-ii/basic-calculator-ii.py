class Solution:
    def calculate(self, s: str) -> int:
        s += '+0'
        stack, op, num = [], '+', 0
        for ch in s:
            if ch == ' ': continue
            if ch.isdigit():
                num = num*10 + int(ch)
            else:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / float(num)))
                op, num = ch, 0
        return sum(stack)