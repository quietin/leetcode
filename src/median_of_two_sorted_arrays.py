def find_kth(list_a, list_b, k):
    len_a, len_b = len(list_a), len(list_b)

    # make sure that len_a <= len_b in order to only handle list_a
    if len_a > len_b:
        return find_kth(list_b, list_a, k)

    if len_a == 0:
        return list_b[k - 1]

    if k == 1:
        return min(list_a[0], list_b[0])

    # k/2 may bigger than len_a, get the smaller one and keep pos_a + pos_b = k
    pos_a = min(len_a, k / 2)
    pos_b = k - pos_a

    val_a, val_b = list_a[pos_a - 1], list_b[pos_b - 1]
    if val_a < val_b:
        return find_kth(list_a[pos_a:], list_b, k - pos_a)
    elif val_a > val_b:
        return find_kth(list_a, list_b[pos_b:], k - pos_b)
    else:
        return list_a[pos_a - 1]


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a_len, b_len = len(nums1), len(nums2)
        total = a_len + b_len
        half = total / 2
        if total & 1:
            return find_kth(nums1, nums2, half + 1)
        else:
            return (find_kth(nums1, nums2, half) + find_kth(nums1, nums2, half + 1)) / 2.0
