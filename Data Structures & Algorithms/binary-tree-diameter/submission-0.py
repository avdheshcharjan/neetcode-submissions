# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # max (left subtree, right subtree)
        #can be done through recursion + DFS

        #height =/= diameter; medium question NOT EASY

        self.res=0 # can also res=0 but then declare on line 19 'nonlocal res'
        #returns height:
        def dfs(curr):
            if not curr:
                return 0
            
            left=dfs(curr.left)
            right=dfs(curr.right)

            self.res=max(self.res, left+ right)
            return max(left,right) + 1
        #call recursive function:
        dfs(root)
        return self.res

