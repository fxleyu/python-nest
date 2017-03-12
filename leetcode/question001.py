class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for index,item in enumerate(nums):
            other = target - item
            if map.has_key(other):
                return [map[other], index]
            else:
                map[item] = index
        return []

if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums,target))
