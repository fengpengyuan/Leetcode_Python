__author__ = 'fengpeng'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head

        ppre, pre, cur = dummy, head, head.next

        while cur:
            pnext = cur.next
            ppre.next = cur
            cur.next = pre
            pre.next = pnext

            cur = pnext
            ppre = pre
            pre = cur
            if cur:
                cur = cur.next
        return dummy.next


    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        node = head.next

        head.next = self.swapPairs(head.next.next)
        node.next = head
        return node


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

node = Solution().swapPairs(head)

while node:
    print node.val,
    node = node.next