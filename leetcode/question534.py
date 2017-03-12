import random

class Codec:
    STRING = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    map = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        tag = self.gen_tag()
        self.map[tag] = longUrl
        return "http://tinyurl.com/" + tag

    def gen_tag(self):
        tag = self.gen_random_str()
        while self.map.has_key(tag):
            tag = self.gen_random_str()
        return tag

    def gen_random_str(self):
        result = ""
        for i in xrange(6):
            result += self.STRING[random.randint(0,61)]
        return result

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.map[shortUrl[-6:]]


if __name__ == '__main__':
    code = Codec()
    print len(code.STRING)
    longth = "https://leetcode.com/problems/design-tinyurl"
    short = code.encode("https://leetcode.com/problems/design-tinyurl")
    print longth
    print short
    print code.decode(short)
