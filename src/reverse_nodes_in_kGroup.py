# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head

        l_len = 0
        head_dummy = head
        while head:
            head = head.next
            l_len += 1
        reverse_time = l_len / k

        if reverse_time < 1:
            return head_dummy

        prev = None
        head = head_dummy
        start = tail = head
        first = True
        while reverse_time:
            cur = start.next
            count = 1
            while count < k and cur:
                tmp = cur.next
                start.next = tmp
                cur.next = tail
                tail = cur
                cur = tmp
                count += 1

            if first:
                head = tail
                first = False
            if prev:
                prev.next = tail

            prev = start
            start = tail = cur
            reverse_time -= 1
        return head
