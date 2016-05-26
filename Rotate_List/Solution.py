__author__ = 'fengpeng'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k < 1:
            return head
        l = self.getLength(head)
        k %= l
        if k == 0:
            return head
        fast, slow = head, head
        for i in xrange(k):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        newHead = slow.next
        slow.next = None
        fast.next = head

        return newHead

    def getLength(self, head):
        cur, count = head, 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        count = 0
        while fast.next:
            count += 1
            fast = fast.next
        for i in xrange(count - k % count):
            slow = slow.next

        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None

        return dummy.next

    # without dummy node
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast, slow = head, head
        count = 1
        while fast.next:
            count += 1
            fast = fast.next
        for i in xrange(count - k % count):
            slow = slow.next
        fast.next = head
        newHead = slow.next
        slow.next = None

        return newHead

    # make a circle
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast = head
        count = 1
        while fast.next:
            count += 1
            fast = fast.next

        fast.next = head
        for i in xrange(count - k % count):
            fast = fast.next
        newHead = fast.next
        fast.next = None

        return newHead


head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

res = Solution().rotateRight(head, 2)

while res:
    print res.val,
    res = res.next