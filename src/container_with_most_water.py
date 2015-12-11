class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1

        ret = 0
        while left < right:
            result = min(height[left], height[right]) * (right - left)
            if result > ret:
                ret = result
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ret
