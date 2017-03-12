class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        half = len(string)/2
        for i in xrange(half):
            if string[i] != string[-1-i]:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    print solution.isPalindrome(-123)
    print solution.isPalindrome(-123321)
    print solution.isPalindrome(123321)
    print solution.isPalindrome(0)
