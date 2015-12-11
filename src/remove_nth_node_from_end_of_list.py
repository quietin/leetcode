# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def reverse(r):
    if r.next is None:
        return r

    head = tail = r
    cur = r.next
    while cur:
        tmp = cur.next
        head.next = tmp
        cur.next = tail
        tail = cur
        cur = tmp

    return tail


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        r_node = reverse(head)
        r_fake = r_node
        prev = None

        while n > 1:
            prev = r_node
            r_node = r_node.next
            n -= 1

        if prev is None:
            r_fake = r_fake.next
        else:
            prev.next = r_node.next

        if r_fake is None:
            return None
        elif r_fake.next is None:
            return r_fake

        return reverse(r_fake)
