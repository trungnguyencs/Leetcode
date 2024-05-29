class Solution:
    def numSteps(self, s: str) -> int:
        stack = list(s)
        step = 0
        while not stack == ['1']:
            if stack[-1] == '0':
                stack.pop()
                step += 1
            else:
                # '111' -> '1000' -> '1' (1 + 3 = 4 steps)
                step += 1
                while stack and stack[-1] == '1':
                    stack.pop()
                    step += 1
                if stack:
                    stack[-1] = '1'
                else:
                    stack.append('1')
        return step