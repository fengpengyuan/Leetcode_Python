__author__ = 'fengpeng'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        fast, slow = head, head
        # while fast and fast.next:
        # fast = fast.next.next
        #     if not fast:
        #         break
        #     slow = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondHalf = slow.next
        slow.next = None

        secondHalf = self.reverseList(secondHalf)
        cur1, cur2 = head, secondHalf
        while cur1 and cur2:
            pnext1 = cur1.next
            pnext2 = cur2.next
            cur1.next = cur2
            cur2.next = pnext1

            cur1 = pnext1
            cur2 = pnext2


    def reverseList(self, head):
        if not head or not head.next:
            return head
        pre, cur = None, head

        while cur:
            pnext = cur.next
            cur.next = pre
            pre = cur
            cur = pnext
        return pre


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)

Solution().reorderList(head)

while head:
    print head.val,
    head = head.next
