class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h, n = len(haystack), len(needle)
        if not n:
            return 0
        if not h or h < n:
            return -1

        # use kmp _next arr
        _next = [0] * n

        def kmp_next():
            _next[0] = -1
            a, b = 0, -1
            while a < n - 1:
                if b == -1 or needle[a] == needle[b]:
                    a += 1
                    b += 1
                    if needle[a] == needle[b]:
                        _next[a] = _next[b]
                    else:
                        _next[a] = b
                else:
                    b = _next[b]

        kmp_next()
        i, j = 0, 0
        while i < h and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = _next[j]

        if j == n:
            return i - j

        return -1
