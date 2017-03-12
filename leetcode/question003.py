class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        start = 0
        for i in range(1, len(s)):
            index = self.indexOfRepeatChar(s, start, i)
            if index != -1:
                thisMax = i - start
                start = index + 1
                if thisMax > max:
                    max = thisMax
        thisMax = len(s) - start
        if thisMax > max:
            max = thisMax
        return max

    def indexOfRepeatChar(self, s, start, end):
        for i in reversed(range(start, end)):
            if s[i] == s[end]:
                return i
        else:
            return -1



if __name__ == '__main__':
    solution = Solution()
    print solution.lengthOfLongestSubstring("abcabcbb")
    print solution.lengthOfLongestSubstring("bbbbb")
    print solution.lengthOfLongestSubstring("")
    print solution.lengthOfLongestSubstring("dvdf")
