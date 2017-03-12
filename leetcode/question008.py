class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        toValue = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

        start = 0
        for i in xrange(len(str)):
            if  str[i] == "+" or str[i] == "-":
                start = i + 1
                break
            elif toValue.has_key(str[i]):
                start = i
                break
            elif str[i] != " ":
                return 0

        value = 0
        for i in xrange(start, len(str)):
            if toValue.has_key(str[i]):
                value = value * 10 + toValue.get(str[i])
            else:
                break

        if start != 0 and str[start-1] == "-":
            value *= -1;
        if value > 2147483647:
            value = 2147483647
        elif value < -2147483648:
            value = -2147483648
        return value

if __name__ == '__main__':
    solution = Solution();
    print solution.myAtoi("   +001")
    print solution.myAtoi("   2147483648  ")
    print solution.myAtoi("  -0012a42")
    print solution.myAtoi("-1234")
