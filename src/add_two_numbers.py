# Definition for singly-linked list.
# class ListNode(object):
#      def __init__(self, x):
#          self.val = x
#          self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        new_node = ListNode(0)
        temp = new_node
        pro_num = 0

        while l1 and l2:
            pro_num, new_node.val = divmod(l1.val + l2.val + pro_num, 10)
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                new_node.next = ListNode(0)
                new_node = new_node.next

        ls = l1 or l2 or None

        while ls:
            pro_num, new_node.val = divmod(ls.val + pro_num, 10)
            if ls.next:
                new_node.next = ListNode(0)
                new_node = new_node.next
                ls = ls.next
            else:
                break

        if pro_num:
            new_node.next = ListNode(pro_num)

        return temp
