class Codec:

    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits
        self.baseUrl = 'tinyurl.com/'
        self.urlToCode = {}
        self.codeToUrl = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.urlToCode:
            code = self.urlToCode[longUrl]
        else:
            code = self._generateRandomCode()
            while code in self.codeToUrl:
                code = self._generateRandomCode()
            self.urlToCode[longUrl] = code
            self.codeToUrl[code] = longUrl
        return self.baseUrl + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl[-6:]
        return self.codeToUrl[code]
        
    def _generateRandomCode(self):
        code = ''
        for _ in range(6):
            code += random.choice(self.alphabet)
        return code

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))