class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 1
        if x < 0:
            x = -x
            negative = -1

        l = []
        while x:
            x, y = divmod(x, 10)
            l.append(y)

        my_num = 0
        zero_flag = True
        for x in xrange(len(l)):
            val = l[x]
            if not val:
                if zero_flag:
                    continue
            else:
                zero_flag = False

            my_num = my_num * 10 + val

        my_num *= negative
        max_int = 2 ** 31 - 1
        return my_num if -max_int - 1 < my_num < max_int else 0
