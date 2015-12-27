class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # use bitwise operation
        if divisor == 0:
            return -1

        is_neg = (dividend ^ divisor) >> 31
        dividend = abs(dividend)
        divisor = abs(divisor)
        digit = 0
        while divisor <= (dividend >> 1):
            divisor <<= 1
            digit += 1

        ret = 0
        while digit >= 0:
            if dividend >= divisor:
                dividend -= divisor
                ret += 1 << digit
            divisor >>= 1
            digit -= 1

        max_int = 2 ** 31
        if ret >= max_int:
            return -max_int if is_neg else max_int - 1

        return -ret if is_neg else ret
