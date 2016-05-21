__author__ = 'fengpeng'


# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        if root.left:
            root.left.next=root.right
        if root.right:
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        start = root
        while start:
            cur = start
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.next and cur.right:
                    cur.right.next = cur.next.left
                cur = cur.next
            start = start.left
