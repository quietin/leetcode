# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        left = head
        right = head.next
        head = right
        while right:
            tmp = right.next
            left.next = tmp
            right.next = left
            prev_r = left
            left = left.next

            if not left or not left.next:
                break
            else:
                right = left.next
                prev_r.next = right

        return head
