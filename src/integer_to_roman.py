class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        while num:
            num, remainder = divmod(num, 10)
            res.append(remainder)

        if res[-1] == 0:
            res.pop()

        roma = ''
        convert = [
            ['I', 'V'], ['X', 'L'], ['C', 'D'], ['M']
        ]
        for x in xrange(len(res)):
            x_val = res[x]
            if x_val == 0:
                continue
            else:
                if x_val >= 4:
                    if x_val == 9:
                        buf = convert[x][0] + convert[x + 1][0]
                    elif x_val == 4:
                        buf = convert[x][0] + convert[x][1]
                    else:
                        buf = convert[x][1] + (x_val - 5) * convert[x][0]

                else:
                    buf = x_val * convert[x][0]

                roma = buf + roma

        return roma
