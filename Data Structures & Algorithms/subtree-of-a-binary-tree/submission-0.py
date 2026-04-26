# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        # if not root and not subRoot:
        #     return True
        
        # left=root.left
        # right=root.right
        # while()
        # if root.val <subRoot.val:
        #     root.left
        # elif root.val > subRoot.val:
        #     root.right
        # else:
        #     return root.left!=subRoot.left or root.right!=subRoot.right
        
        # return isSubtree(root.left,subRoot.left) and isSubtree(root.right, subRoot.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        # return self.isSubtree(root.left, subRoot.left) or self.isSubtree(root.right, subRoot.left)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    