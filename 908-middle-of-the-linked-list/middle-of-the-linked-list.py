# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.total = 0

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.findMiddleNode(head)
        middle = self.calculateMiddleNode(head)
        return middle

    def findMiddleNode(self, head):
        if head:
            self.total+=1
            if head.next: 
                self.findMiddleNode(head.next)
            
    def calculateMiddleNode(self, head):
        i = 0
        answer = head
        while i<(self.total//2):
            answer = answer.next 
            i+=1
        return answer   