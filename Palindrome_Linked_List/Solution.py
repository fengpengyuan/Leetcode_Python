__author__ = 'fengpeng'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # def isPalindrome(self, head):
    # """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     if not head or not head.next:
    #         return True
    #     len = self.getLength(head)
    #     return self.isPalindromeUtil(head, 0, len - 1)
    #
    # def getLength(self, head):
    #     len = 0
    #     while head:
    #         len += 1
    #         head = head.next
    #     return len
    #
    # def isPalindromeUtil(self, head, start, end):
    #     if not head or not head.next:
    #         return True
    #     cur = head
    #     for i in xrange(start, end):
    #         cur = cur.next
    #     if head.val != cur.val:
    #         return False
    #     return self.isPalindromeUtil(head.next, start + 1, end - 1)

    #########################################################################
    def isPalindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            if not fast:
                break
            slow = slow.next

        head2 = slow.next
        slow.next = None
        head2 = self.reverseList(head2)

        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

    def reverseList(self, head):
        if not head or not head.next:
            return head
        pnext = head.next
        newHead = self.reverseList(pnext)
        pnext.next = head
        head.next = None

        return newHead

    ############################
    # solution 3
    def isPalindrome3(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst = []
        while head:
            lst.append(head)
            head = head.next
        return lst == lst[::-1]


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print Solution().isPalindrome2(head)
