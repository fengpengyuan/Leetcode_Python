__author__ = 'fengpeng'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        return True if fast == slow else False


head = ListNode(1)
head.next = ListNode(2)

Solution().hasCycle(head)