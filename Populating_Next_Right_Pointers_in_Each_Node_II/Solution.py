import collections

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
        que = list()
        que.append(root)
        cur, next = 1, 0
        while que:
            first = que.pop(0)
            cur -= 1
            if cur != 0:
                first.next = que[0]
            if first.left:
                que.append(first.left)
                next += 1
            if first.right:
                que.append(first.right)
                next += 1
            if cur == 0:
                cur = next
                next = 0

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        dummy = TreeLinkNode(0)
        pre = dummy
        while root:
            if root.left:
                pre.next = root.left
                pre = pre.next
            if root.right:
                pre.next = root.right
                pre = pre.next
            root = root.next
            if not root:
                pre = dummy
                root = dummy.next
                dummy.next = None

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        cur = root
        while cur:
            nextlevel, pre = None, None
            while cur:
                if not nextlevel:
                    nextlevel = cur.left if cur.left else cur.right
                if cur.left:
                    if pre:
                        pre.next = cur.left
                        pre = pre.next
                    else:
                        pre = cur.left

                if cur.right:
                    if pre:
                        pre.next = cur.right
                        pre = pre.next
                    else:
                        pre = cur.right
                cur=cur.next
            cur = nextlevel


