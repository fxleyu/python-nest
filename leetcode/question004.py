# -*- coding: utf-8 -*-
import sys

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        mid = length / 2
        if length % 2 == 1:
            mid += 1

        index1 = index2 = 0
        result = 0
        for i in xrange(mid) :
            a = self.getIndex(nums1, index1)
            b = self.getIndex(nums2, index2)
            if a < b:
                index1 += 1
                result = a
            else:
                index2 += 1
                result = b

        if length % 2 == 1:
            return result / 1.0

        a = self.getIndex(nums1, index1)
        b = self.getIndex(nums2, index2)
        if a < b:
            result += a
        else:
            result += b
        return result / 2.0

    def getIndex(self, nums, index):
        if len(nums) > index :
            return nums[index]
        else :
            return sys.maxint

if __name__ == '__main__':
    solution = Solution()
    print solution.findMedianSortedArrays([1, 2], [3, 4])
    print solution.findMedianSortedArrays([1, 3],[2])
    print solution.findMedianSortedArrays([1, 3], [])
    print solution.findMedianSortedArrays([], [1,2,3])
