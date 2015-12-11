class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        s = strs[0]
        for cur_str in strs[1:]:
            j = 0
            while j < len(s) and j < len(cur_str):
                if s[j] == cur_str[j]:
                    j += 1
                else:
                    break

            s = s[0:j]

        return s
