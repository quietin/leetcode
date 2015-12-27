# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        import heapq

        new_node = ListNode(-1)
        new_fake = new_node
        data = []
        while True:
            stop = True
            for index, item in enumerate(lists):
                if item:
                    stop = False
                    heapq.heappush(data, item.val)
                    lists[index] = lists[index].next

            if stop:
                break

        data_len = len(data)
        if data_len:
            for _ in xrange(data_len):
                new_node.next = ListNode(0)
                new_node = new_node.next
                new_node.val = heapq.heappop(data)

        return new_fake.next
