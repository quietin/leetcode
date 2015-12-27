class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = len(nums) - 1

        while r > 0:
            if nums[r] == nums[r - 1]:
                del nums[r]
            r -= 1

        return len(nums)
