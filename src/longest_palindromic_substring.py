class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        if not s_len:
            return ""

        res_left, res_right, x, count, max_len = [0] * 5

        def process(left, right):
            l = r = 0
            while left >= 0 and right < s_len:
                if s[left] == s[right]:
                    l, r = left, right
                    left -= 1
                    right += 1
                else:
                    break

            return l, r, r - l + 1

        left, right, dis = 0, 0, 1
        is_odd = s_len & 1
        while x < s_len:
            # if left string length cannot make up longer str, jump out of loop
            if is_odd:
                if (s_len - x) * 2 - 1 <= max_len:
                    break
            else:
                if (s_len - x) * 2 <= max_len:
                    break

            if x + 1 < s_len:
                if s[x] == s[x + 1]:
                    left, right, dis = process(x, x + 1)
                else:
                    left, right, dis = process(x, x)

            if dis > max_len:
                max_len = dis
                res_left, res_right = left, right

            x += 1

        return s[res_left:res_right + 1]
