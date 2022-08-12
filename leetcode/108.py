class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(node, nums):
            mid = len(nums) // 2
            l = 0
            r = len(nums) - 1
            
            if l > r:
                return None
            
            node = TreeNode(nums[mid])
            
            node.left = dfs(node, nums[:mid])
            node.right = dfs(node, nums[mid+1:])
            
            return node
            
        return dfs(TreeNode(), nums)