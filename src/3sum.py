class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r_len = len(nums)
        if r_len < 3:
            return []

        res = sorted(nums)
        ret = []
        i = 0

        def left_stop(left, right):
            left += 1
            while left < right - 1:
                if res[left] == res[left - 1]:
                    left += 1
                else:
                    break
            return left

        def right_stop(left, right):
            right -= 1
            while left < right - 1:
                if res[right] == res[right + 1]:
                    right -= 1
                else:
                    break
            return right

        while i < r_len - 2:
            first = i
            left = i + 1
            right = r_len - 1

            while left < right:
                ele_list = [res[first], res[left], res[right]]
                total = sum(ele_list)
                if total == 0:
                    ret.append(ele_list)
                    left = left_stop(left, right)
                    right = right_stop(left, right)
                elif total < 0:
                    left = left_stop(left, right)
                else:
                    right = right_stop(left, right)

            while i + 1 < r_len - 2:
                if res[i] == res[i + 1]:
                    i += 1
                else:
                    break

            i += 1

        return ret
