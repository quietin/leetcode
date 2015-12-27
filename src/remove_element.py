class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        r = len(nums) - 1
        while r >= 0:
            if nums[r] == val:
                del nums[r]
            r -= 1
        return len(nums)
