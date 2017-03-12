class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        result = []
        indexs = []
        for i in xrange(0, len(s), 2*numRows - 2):
            result.append(s[i])
            indexs.append(i)

        for i in xrange(1, numRows):
            for top in indexs:
                one = top + i
                two = top + i + 2 * (numRows - 1 - i)
                self.insert(result, s, one)
                if one != two:
                    self.insert(result, s, two)
        return "".join(result)

    def insert(self, result, s, index):
        if index < len(s):
            result.append(s[index])

    def convert1(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            print "L", L
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
            print "index", index

        return ''.join(L)

if __name__ == '__main__':
    solution = Solution()
    print solution.convert1("PAYPALISHIRING", 3)
    print solution.convert1("ABCD", 3)
