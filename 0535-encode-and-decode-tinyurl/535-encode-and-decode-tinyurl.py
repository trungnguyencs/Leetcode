class Codec:

    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits
        self.url2Code, self.code2Url = {}, {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.url2Code:
            code = ''.join([choice(self.alphabet) for _ in range(6)])
            if code not in self.code2Url:
                self.code2Url[code] = longUrl
                self.url2Code[longUrl] = code
        return "http://tinyurl.com/" + self.url2Code[longUrl]
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code2Url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))