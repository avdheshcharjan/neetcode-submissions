# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # temp=TreeNode()
        # # while root.left.val<root.right.val:
        # #     root.right=root.left
        # # while root.left.val>
        # if root.right.val>root.left.val:
        #     # temp=root.left
        #     root.left=root.right
        #     # root.right=root.left
        #     # self.invertTree(root)

        # APPROACH WAS RIGHT BUT THE RECURSION SODOMIZED ME!!!! AAAAAAAH!!!!
        temp=root.left
        root.left=root.right
        root.right=temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

