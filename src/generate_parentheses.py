class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['()']
        elif n == 2:
            return ['()()', '(())']

        last = self.generateParenthesis(n - 1)
        left = ['()' + k for k in last]
        mid = ['(' + k + ')' for k in last]
        right = [k + '()' for k in last]
        res = left + mid + right

        if n // 2 - 1 >= 1:
            for k in xrange(1, n // 2 + 1):
                a = self.generateParenthesis(k)
                if k != n - k:
                    b = self.generateParenthesis(n - k)
                else:
                    b = a
                tmp = []
                for t in a:
                    for m in b:
                        tmp.append(t + m)
                        tmp.append(m + t)
                res += list(set(tmp))

        return list(set(res))
