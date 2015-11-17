class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        if not s:
            return max_len

        store = {}
        s_len = len(s)
        start, end = 0, 0
        new_start = 0

        while start < s_len:

            while new_start <= end < s_len:

                if s[end] not in store:
                    store[s[end]] = end
                    temp_len = end - start + 1
                    if temp_len > max_len:
                        max_len = temp_len
                    end += 1
                else:
                    # offset+1
                    old_start, new_start = start, end + 1

                    # set new start for length account
                    start = store[s[end]] + 1

                    # pop some keys which not exists in hashtable(dict)
                    for j in xrange(old_start, start, 1):
                        # del is a little faster than pop
                        del store[s[j]]

                    store[s[end]] = end
                    end = new_start
                    break

            if s_len - start <= max_len or new_start == s_len:
                break

        return max_len
