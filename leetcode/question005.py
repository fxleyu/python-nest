class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max = 0
        index = 0

        for i in xrange(0, len(s)):
            len1 = self.length_of_prlindrome(s, i, i)
            len2 = self.length_of_prlindrome(s, i, i + 1)
            if len1 > max:
                max = len1
                index = i - len1 / 2
            if len2 > max:
                max = len2
                index = i - len2 / 2 + 1
        return s[index : index + max]

    def length_of_prlindrome(me, s, left, right):
        result = 1
        for i in xrange(0, left+1):
            if right + i >= len(s) or s[left - i] != s[right + i]:
                # right + i -1 - (left - i + 1) + 1 == right - left + 2*i -1
                result = right - left + 2*i -1
                break
        else:
            result = right + left + 1
        return result

if __name__ == '__main__':
    solution = Solution()
    print solution.longestPalindrome("a")
    print solution.longestPalindrome("cbbd")
    print solution.longestPalindrome("babad")
    print solution.longestPalindrome("")
