# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # curr = root
        # lengL=lenR=0
        # while root.right:
        #     curr=root.right
        #     lenR+=1
        

        # while root.left:
        #     curr=root.left
        #     lenL+=1
        # return max(lenL, lenR)

        leftH=self.maxDepth(root.left)
        rightH=self.maxDepth(root.right)

        return max(leftH, rightH)+1
