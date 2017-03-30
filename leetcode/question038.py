class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return 0

        i = 1
        result = 1
        while i < n:
            result = self.gen_next_number(result)
            i += 1
        return str(result)

    def gen_next_number(self, n):
        s = str(n)

        now = s[0]
        num = 1
        result = ""
        for i in xrange(1, len(s)):
            if s[i] == now:
                num += 1
            else:
                result += str(num) + now
                num = 1
                now = s[i]
        result += str(num) + now
        return int(result)

if __name__ == '__main__':
    solution = Solution()
    print solution.countAndSay(3)
    print solution.countAndSay(1)
    print solution.countAndSay(2)
    print solution.countAndSay(0)
