__author__ = 'fengpeng'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            if not fast:
                break
            slow = slow.next
        head2 = slow.next
        slow.next = None

        head1 = self.sortList(head)
        head2 = self.sortList(head2)

        return self.merge(head1, head2)

    def merge(self, head1, head2):
        if not head1 or not head2:
            return head2 if not head1 else head1
        dummy = pre = ListNode(0)

        while head1 and head2:
            if head1.val < head2.val:
                pre.next, head1 = head1, head1.next
            else:
                pre.next, head2 = head2, head2.next
            pre = pre.next
        if head1:
            pre.next = head1
        if head2:
            pre.next = head2
        return dummy.next


head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(1)
head.next.next.next = ListNode(7)

cur = Solution().sortList(head)
while cur:
    print cur,
    cur = cur.next