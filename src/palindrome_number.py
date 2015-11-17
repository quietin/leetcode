class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # reverse the integer first
        if x < 0:
            return False
        elif x == 0:
            return True

        y = x
        ret = 0
        while y != 0:
            ret = 10 * ret + y % 10
            y //= 10

        while x != 0 or ret != 0:
            if x % 10 == ret % 10:
                x //= 10
                ret //= 10
            else:
                break

        if x == ret == 0:
            return True

        return False
