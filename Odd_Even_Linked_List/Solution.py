__author__ = 'fengpeng'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        pass

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummyOdd = preOdd = ListNode(0)
        dummyEven = preEven = ListNode(0)
        cur = head
        idx = 1
        while cur is not None:
            if idx % 2 == 0:
                preEven.next = cur
                preEven = preEven.next
            else:
                preOdd.next = cur
                preOdd = preOdd.next
            cur = cur.next
            idx += 1
        preEven.next = None
        preOdd.next = dummyEven.next
        return dummyOdd.next

    def oddEvenList2(self, head):
        if not head or not head.next:
            return head
        odd, even, evenHead = head, head.next, head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead
        return head


head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)

Solution().oddEvenList2(head)


