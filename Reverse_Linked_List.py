__author__ = 'fengpeng'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pnext = head.next
        t = self.reverseList2(pnext)
        pnext.next = head
        head.next = None
        return t
