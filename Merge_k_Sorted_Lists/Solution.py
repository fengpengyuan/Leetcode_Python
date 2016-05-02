import heapq

__author__ = 'fengpeng'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res, heap = [], []
        for lst in lists:
            while lst:
                heapq.heappush(heap, lst.val)
                lst = lst.next
        while heap:
            res.append(heapq.heappop(heap))
        return res

    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) / 2
        left = self.mergeKLists(lists[: mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)

    def merge(self, list1, list2):
        if not list1 or not list2:
            return list1 if not list2 else list2
        dummy = pre = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2;
                list2 = list2.next
            pre = pre.next
        pre.next = list1 if list1 else list2

        return dummy.next
