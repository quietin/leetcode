class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        convert = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }
        x = ret = 0

        while x < len(s):

            start = x
            while x + 1 < len(s):
                if s[x] == s[x + 1]:
                    x += 1
                else:
                    break

            sign = 1
            if x + 1 < len(s):
                if convert[s[x + 1]] // convert[s[x]] in [10, 5]:
                    sign = -1

            ret += (x - start + 1) * convert[s[x]] * sign
            x += 1

        return ret
