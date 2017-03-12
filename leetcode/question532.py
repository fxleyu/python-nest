class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        handle_set = set()
        result_set = set()
        for num in nums:
            if num -k in handle_set:
                result_set.add(num -k)
            if num + k in handle_set:
                result_set.add(num)
            handle_set.add(num)

        return len(result_set)

if __name__ == '__main__':
    solute = Solution()
    print solute.findPairs( [3, 1, 4, 1, 5], k = 2)
    print solute.findPairs([1, 2, 3, 4, 5], k = 1)
    print solute.findPairs([1, 3, 1, 5, 4], k = 0)
