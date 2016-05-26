__author__ = 'fengpeng'


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, cur = head, head.next
        unique = set([head.val])
        while cur:
            if cur.val in unique:
                pre.next = cur.next
            else:
                unique.add(cur.val)
                pre = cur
            cur = cur.next
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(1)

res = Solution().removeDuplicates(head)

while res:
    print res.val,
    res = res.next
