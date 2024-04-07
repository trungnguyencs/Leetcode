class Solution:
    def checkValidString(self, s: str) -> bool:
        # # O(n) time O(n) space solution: 2 stacks: one for '(', one for '*'
        # s1, s2 = [], []
        # for i, ch in enumerate(s):
        #     if ch == '(':
        #         s1.append(i)
        #     elif ch == '*':
        #         s2.append(i)
        #     elif s1:
        #         s1.pop()
        #     elif s2:
        #         s2.pop()
        #     else:
        #         return False
        # while s1 and s2:
        #     if s1.pop() > s2.pop():
        #         return False
        # return len(s1) == 0
        
        # O(n) time O(1) space solution: count '(' in the range [minOpen, maxOpen]
        maxOpen = 0 # maxOpen takes care of ')' without prior '('
        minOpen = 0 # minOpen takes care of '(' with no closing ')'
        for ch in s:
            if ch == '(':
                maxOpen += 1
                minOpen += 1
            elif ch == ')':
                maxOpen -= 1
                minOpen -= 1 if minOpen > 0 else 0
            else:
                maxOpen += 1
                minOpen -= 1 if minOpen > 0 else 0
            if maxOpen < 0: return False
        return minOpen == 0