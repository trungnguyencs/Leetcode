class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        #greedy: assuming x > y so we remove all 'ab' then remove all 'ba'
        ab, ba = ['a', 'b'], ['b', 'a']
        if x < y: return self.helper(s, y, x, ba, ab)
        return self.helper(s, x, y, ab, ba)

    def helper(self, s, x, y, ab, ba):
        points = 0
        stack1 = []
        for ch in s:
            stack1.append(ch)
            if stack1[-2:] == ab:
                points += x
                stack1.pop()
                stack1.pop()
        stack2 = [] 
        for ch in stack1:
            stack2.append(ch)
            if stack2[-2:] == ba:
                points += y
                stack2.pop()
                stack2.pop()
        return points