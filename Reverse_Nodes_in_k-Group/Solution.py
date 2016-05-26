__author__ = 'fengpeng'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur, pre = head, dummy
        count = 0
        while cur:
            count += 1
            if count % k == 0:
                pre = self.reverse(pre, cur.next)
            cur = cur.next

        return dummy.next

    # return last node
    def reverse(self, pre, next):
        last = pre.next
        cur = last.next
        while cur != next:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur

            cur = last.next

        return last


pre = ListNode(0)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
next = ListNode(4)

head.next.next.next = next
pre.next = head

res = Solution().reverseKGroup(pre, 3)

while res:
    print res.val,
    res = res.next



