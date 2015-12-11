# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None

        new_l = ListNode(0)
        new_fake = new_l
        while True:

            if l1 and l2:
                if l1.val > l2.val:
                    new_l.val = l2.val
                    l2 = l2.next
                else:
                    new_l.val = l1.val
                    l1 = l1.next
            elif l1:
                new_l.val = l1.val
                l1 = l1.next
            elif l2:
                new_l.val = l2.val
                l2 = l2.next
            else:
                new_l.next = None
                break

            if l1 or l2:
                new_l.next = ListNode(0)
                new_l = new_l.next

        return new_fake
