class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match_dict = {'(': ')', '[': ']', '{': '}'}
        right_part = {')', ']', '}'}
        stack = []
        for c in s:
            if c in right_part:
                if stack and c == match_dict.get(stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False
