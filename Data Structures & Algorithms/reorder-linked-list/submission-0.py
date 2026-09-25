# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        # print(slow.val)
        # print(fast.val)
        prev,cur = None, slow.next
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # while head:
        #     print(head.val, " ")
        #     head = head.next

        # while prev:
        #     print(prev.val, " ")
        #     prev = prev.next
        # head = prev
        # slow.next = None
        # return prev
        cur = head
        while prev:
            temp = cur.next
            ptemp = prev.next
            cur.next = prev
            cur.next.next = temp
            prev = ptemp
            cur = temp
        
        while head:
            print(head.val, " ")
            head = head.next


        # print(prev.val)
        # print(fast.val)