class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fast = slow = head
        
        while fast:
            fast = fast.next.next
            slow = slow.next
        
        firstHalf = []
        while head and head != slow:
            firstHalf.append(head.val)
            head = head.next
        
        secondHalf = []
        while head:
            secondHalf.append(head.val)
            head = head.next
            
        m = 0
        for i, j in zip(firstHalf, secondHalf[::-1]):
            m = max(m, i+j)
        
        return m