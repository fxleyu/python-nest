class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        row = self.find_row(picture)
        column =self.find_colum(picture)

        result = 0
        for x in row:
            for y in column:
                if picture[x][y] == "B":
                    result += 1
        return result

    def find_row(self, picture):
        result = []
        for x in xrange(len(picture)):
            num = 0
            for y in xrange(len(picture[x])):
                if picture[x][y] == "B":
                    num += 1
            if num == 1:
                result.append(x)
        return result

    def find_colum(self, picture):
        result = []
        for y in xrange(len(picture[0])):
            num = 0
            for x in xrange(len(picture)):
                if picture[x][y] == "B":
                    num += 1
            if num == 1:
                result.append(y)
        return result


if __name__ == '__main__':
    solute = Solution()
    print solute.findLonelyPixel([['W', 'W', 'B'],['W', 'B', 'W'], ['B', 'W', 'W']])
