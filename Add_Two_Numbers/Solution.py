__author__ = 'fengpeng'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def addTwoNumbers(self, l1, l2):
        if l1 is None or l2 is None:
            return l2 if l1 is None else l1
        dummy = pre = ListNode(0)
        carry = 0
        while l1 is not None or l2 is not None:
            num1 = 0 if l1 is None else l1.val
            num2 = 0 if l2 is None else l2.val
            s = num1 + num2 + carry
            carry = s / 10
            s %= 10
            pre.next = ListNode(s)
            pre = pre.next
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        if carry == 1:
            pre.next = ListNode(1)
        return dummy.next