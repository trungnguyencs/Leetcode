class Solution:
    def decodeString(self, s: str) -> str:
        curS, curNum, stack = '', 0, []
        for ch in s:
            if ch.isdigit():
                curNum = curNum * 10 + int(ch)
            elif ch.isalpha():
                curS += ch
            elif ch == '[':
                stack.append((curNum, curS))
                curNum, curS = 0, ''
            elif ch == ']':
                prevNum, prevS = stack.pop()
                curS = prevS + curS * prevNum
        return curS        