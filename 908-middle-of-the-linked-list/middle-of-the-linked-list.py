# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        temp = head
        while temp != None:
            c+=1
            temp = temp.next
        mid = c//2
        temp = head
        x = 0
        while temp != None:
            if x==mid:
                return temp
            temp = temp.next
            x+=1
            