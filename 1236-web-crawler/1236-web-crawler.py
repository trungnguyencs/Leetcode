# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        host = self.getHost(startUrl)
        q = deque([startUrl])
        visited = {startUrl}
        ans = []
        while q:
            cur = q.popleft()
            if self.getHost(cur) == host:
                ans.append(cur)
            nxt = set(url for url in htmlParser.getUrls(cur) if url not in visited and self.getHost(url) == host)
            q.extend(nxt)
            visited.update(nxt)
        return sorted(ans)
    
    def getHost(self, url):
        host = url.split('//')[1].split('/')[0]
        return host