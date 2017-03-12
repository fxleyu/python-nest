import collections
class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        row_map = {}
        for row in picture:
            if row.count("B") == N:
                row_tuple = tuple(row)
                if row_map.has_key(row_tuple):
                    row_map[row_tuple] += 1
                else:
                    row_map[row_tuple] = 1

        cols = []
        for c in zip(*picture):
            cols.append(1 if c.count("B") == N else 0)

        result = 0
        for row in row_map.keys():
            if row_map.get(row) == N:
                for i in xrange(len(row)):
                    if row[i] == "B" and cols[i] == 1:
                        result += N
        return result
    def findBlackPixel1(self, picture, N):
        ctr = collections.Counter(map(tuple, picture))
        cols = [col.count('B') for col in zip(*picture)]
        return sum(N * zip(row, cols).count(('B', N))
               for row, count in ctr.items()
               if count == N == row.count('B'))

if __name__ == '__main__':
    solute = Solution()
    print solute.findBlackPixel1([['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'],['W', 'B', 'W', 'B', 'B', 'W'],['W', 'W', 'B', 'W', 'B', 'W']],3 )
    print solute.findBlackPixel1(["WBWBBW","WBWBBW","WBWBBW","BWBWWB"], 3)
    print solute.findBlackPixel1(["WBWBBW","WBWBBW","WBWBBW","WWBWBW"], 3)
    print solute.findBlackPixel1(["WBWBBW","BWBWWB","WBWBBW","BWBWWB","WBWBBW","BWBWWB"], 3)
