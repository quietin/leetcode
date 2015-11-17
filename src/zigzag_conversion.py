class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""

        r_list = [[] for _ in xrange(numRows)]
        line_flag = True

        x, s_len = 0, len(s)
        while x < s_len:

            if line_flag:
                line_flag = False

                # handle boundary situation
                stop = min(x + numRows, s_len)
                for y in xrange(x, stop):
                    r_list[y - x].append(s[y])
                x += numRows
            else:
                line_flag = True
                # avoid stop < 0 when numRows = 1
                stop = min(x + numRows - 3, s_len - 1)
                stop = max(stop, 0)

                for y in xrange(x, stop + 1):
                    # be careful to count the Boundary index
                    r_list[numRows - (y - x + 1) - 1].append(s[y])
                x += max(0, numRows - 2)

        return "".join([x for l in r_list for x in l])
