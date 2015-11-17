class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List
        """
        table = {}
        for index, v in enumerate(nums):
            if v in table:
                table[v] = [table[v], index + 1]
                continue

            table[v] = index + 1

        nums.sort()
        start, end = 0, len(nums) - 1
        while start < end:
            result = nums[start] + nums[end]
            if result > target:
                end -= 1
            elif result < target:
                start += 1
            else:
                a = table[nums[start]]
                if isinstance(a, list):
                    a.sort()
                    return a
                b = table[nums[end]]
                return [a, b] if a < b else [b, a]
