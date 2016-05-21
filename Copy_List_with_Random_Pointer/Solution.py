__author__ = 'fengpeng'


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        dict = {}

        cur = head
        while cur:
            copy = RandomListNode(cur.label)
            dict[cur] = copy
            cur = cur.next
        cur = head

        while cur:
            if cur.next:
                dict[cur].next = dict[cur.next]
            if cur.random:
                dict[cur].random = dict[cur.random]
            cur = cur.next
        return dict[head]

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        cur = head
        while cur:
            copy = RandomListNode(cur.label)
            pnext = cur.next
            cur.next = copy
            copy.next = pnext
            cur = pnext
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        clone = head.next
        cur1 = head
        cur2 = clone
        while cur1:
            cur1.next = cur2.next
            if cur1.next:
                cur2.next = cur1.next.next

            cur1 = cur1.next
            cur2 = cur2.next
        return clone




