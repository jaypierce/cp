class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        sorted_arr = []
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            sorted_arr.append(root.val)
            inorder(root.right)
            
        def build(sorted_arr):
            if not sorted_arr:
                return
            
            l, r = 0, len(sorted_arr)
            mid = (l+r) // 2
            
            root = TreeNode(sorted_arr[mid])
            
            root.left = build(sorted_arr[:mid])
            root.right = build(sorted_arr[mid+1:])
            
            return root
            
        inorder(root)
        return build(sorted_arr)