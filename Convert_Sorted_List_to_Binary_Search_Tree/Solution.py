__author__ = 'fengpeng'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        n = self.getLength(head)
        return self.helper(head, 0, n - 1)

    def helper(self, head, start, end):
        if not head or start > end:
            return None
        m = (start + end) / 2
        cur = head
        for i in xrange(start, m):
            cur = cur.next
        t = cur.next
        cur.next = None
        root = TreeNode(cur.val)
        root.left = self.helper(head, start, m - 1)
        root.right = self.helper(t, m + 1, end)
        return root

    def getLength(self, head):
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        return n

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print root.val,
        self.inorder(root.right)


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        slow, fast, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if pre:
            pre.next = None
        else:
            head = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

    node = None

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        n =self.getLength(head)
        self.node = head

        return self.listToBST(0, n-1)

    def listToBST(self, start, end):
        if start > end:
            return  None

        m = (start+end)/2
        left=self.listToBST(start, m-1)
        root = TreeNode(self.node.val)
        root.left = left
        self.node = self.node.next

        root.right = self.listToBST(m+1, end)
        return root




head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

root = Solution().sortedListToBST(head)

Solution().inorder(root)



