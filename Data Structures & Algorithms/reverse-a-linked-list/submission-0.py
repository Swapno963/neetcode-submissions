# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        if head == None:
            return None
        while(node.next != None):
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        node.next = prev
        head = node

        # nd = head
        # while(nd.next != None):
        #     print(nd.val)

        return head
