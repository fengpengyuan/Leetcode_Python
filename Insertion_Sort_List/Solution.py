__author__ = 'fengpeng'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + " "


class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head

        last, cur = head, head.next
        while cur:
            pre, it = dummy, dummy.next
            while it != cur and it.val < cur.val:
                pre = it
                it = it.next
            if it != cur:
                last.next = cur.next
                pre.next = cur
                cur.next = it
            else:
                last = cur
            cur = last.next
        return dummy.next


head = ListNode(2)
head.next = ListNode(3)
head.next.next = ListNode(1)

cur = Solution().insertionSortList(head)

while cur:
    print cur,
    cur = cur.next
