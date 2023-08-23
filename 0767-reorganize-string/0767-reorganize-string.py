class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        ans = ['']*n
        counter = Counter(s)
        counter = sorted([[count, num] for num, count in counter.items()], reverse=True)
        if counter[0][0] > n//2 + (n % 2): return ''
        i = 0
        for count, c in counter:
            for _ in range(count):
                if i >= len(s): i = 1 #should happen once and only once
                ans[i] = c; i += 2
        return ''.join(ans)