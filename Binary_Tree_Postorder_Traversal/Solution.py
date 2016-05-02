__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stk, cur, pre = [], [], root, None
        while cur:
            stk.append(cur)
            cur = cur.left
        while stk:
            top = stk[-1]
            if top.right and pre != top.right:
                top = top.right
                while top:
                    stk.append(top)
                    top = top.left
            else:
                pre = stk.pop()
                res.append(top.val)
        return res


    # Postorder traversal, which is in Left-Right-Root order.
    # We can observe that the preorder traversal is in Root-Left-Right order,
    # which means if we swap the order of left and right subtree when pushing into stack,
    # we'll get Root-Right-Left, a new traversal.
    def postorderTraversal2(self, root):
        res, stk = [], [root]
        while stk:
            top = stk.pop()
            if top:
                res.insert(0, top.val)
                stk.append(top.left)
                stk.append(top.right)
        return res


root = TreeNode(4)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.left = TreeNode(1)

root.right = TreeNode(6)
root.right.left = TreeNode(5)

print Solution().postorderTraversal(root)
print Solution().postorderTraversal2(root)

