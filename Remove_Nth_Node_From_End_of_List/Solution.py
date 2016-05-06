__author__ = 'fengpeng'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        fast = head
        for i in xrange(n):
            fast = fast.next
        slow, pre = head, dummy

        while fast:
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = slow.next
        return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

Solution().removeNthFromEnd(head, 1)