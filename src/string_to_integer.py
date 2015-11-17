class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # handle '-10', '  -+100', '  -23 4', ' 78 -2ab'...many situation
        s_len = len(str)
        if s_len == 0:
            return 0

        str = str.lstrip()
        net_flag = 1
        ret = start = 0
        first_char = str[0]
        if first_char in ['-', '+']:
            start = 1
            if first_char == '-':
                net_flag = -1
        else:
            if not first_char.isdigit():
                return 0

        for x in xrange(start, len(str)):
            val = str[x]
            if val.isdigit():
                ret = ret * 10 + int(val)
            else:
                break

        max_int = 2 ** 31 - 1
        return max(-max_int - 1, min(max_int, ret * net_flag))
