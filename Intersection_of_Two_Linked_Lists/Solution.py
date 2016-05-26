__author__ = 'fengpeng'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        l1 = self.getLength(headA)
        l2 = self.getLength(headB)
        if l2 > l1:
            headA, headB = headB, headA
        curA = headA
        for i in xrange(abs(l1 - l2)):
            curA = curA.next
        curB = headB

        while curA != curB:
            curA = curA.next
            curB = curB.next
        return curA


    def getLength(self, head):
        cur, l = head, 0
        while cur:
            l += 1
            cur = cur.next
        return l

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        curA, curB = headA, headB

        while curA and curB and curA != curB:
            curA = curA.next
            curB = curB.next
            if curA == curB:
                return curA
            if not curA:
                curA = headB
            if not curB:
                curB = headA
        return None