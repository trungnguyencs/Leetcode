class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # greedy: assuming x > y so remove all 'ab' first then remove all 'ba'
        ab, ba = ['a', 'b'], ['b', 'a']
        if x < y:
            x, y, ab, ba = y, x, ba, ab
        ans = 0
        stack = []
        for ch in s:
            stack.append(ch)
            if stack[-2:] == ab:
                ans += x
                stack.pop()
                stack.pop()
        stack2 = []
        for ch in stack:
            stack2.append(ch)
            if stack2[-2:] == ba:
                ans += y
                stack2.pop()
                stack2.pop()
        return ans