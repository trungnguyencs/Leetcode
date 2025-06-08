class Solution:
    def clearStars(self, s: str) -> str:
        #if there are muliple smallest chars, deleting the right most one will create the smallest string
        #to always has the smallest closest char -> use a heap
        ans = list(s)
        heap = []
        for i, ch in enumerate(s):
            if ch == '*':
                prevCh, prevI = heappop(heap)
                ans[i] = ans[-prevI] = ''
            else:
                heappush(heap, (ch, -i))
        return ''.join(ans)