class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def getMin(node):
            while node.left:
                node = node.left
            return node
            
        
        def dfs(node, key):
            if not node:
                return node
        
            if node.val == key:
                if node.left and node.right:
                    #Find max of right or min in left and make it root
                    tmp = getMin(node.right)
                    node.val = tmp.val
                    node.right = dfs(node.right, tmp.val)
                elif node.left:
                    #Point node to left nodes child
                    node = node.left
                elif node.right:
                    #Point node to right node's child
                    node = node.right
                else:
                    #Point to null
                    node = None
            elif node.val > key:
                node.left = dfs(node.left, key)
            else:
                node.right = dfs(node.right, key)
        
            return node

        return dfs(root, key)