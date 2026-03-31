class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        st = []
        curr = root
        
        while st or curr:
            while curr:
                res.append(curr.val)
                st.append(curr)
                curr = curr.left
            
            curr = st.pop()
            curr = curr.right
        
        return res