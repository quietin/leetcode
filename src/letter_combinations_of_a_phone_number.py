class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r_len = len(nums)
        if r_len < 3:
            return []

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

        res = sorted(nums)
        # set init ret and diff, it's important
        ret = sum(res[:3])
        diff = abs(target - ret)
        i = 0
        stop_flag = False
        while i < r_len - 2:
            first = i
            left = i + 1
            right = r_len - 1

            while left < right:
                total = sum([res[first], res[left], res[right]])
                new_diff = total - target
                if new_diff == 0:
                    ret = total
                    stop_flag = True
                    break
                else:
                    if abs(new_diff) <= diff:
                        diff = abs(new_diff)
                        ret = total
                    if new_diff < 0:
                        left = left_stop(left, right)
                    else:
                        right = right_stop(left, right)

            if stop_flag:
                break

            while i + 1 < r_len - 2:
                if res[i] == res[i + 1]:
                    i += 1
                else:
                    break

            i += 1

        return ret
