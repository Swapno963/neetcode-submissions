# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, cur = None, head
        # reverse the linkdlist        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # while prev:
        #     print(prev.val)
        #     prev = prev.next

        # Remove the element
        # Node can have only one elemet
        temp = prev
        if n == 1:
            # temp = head.next
            prev = prev.next
        else:
            # go to the previous element
            while n - 2:
                # print(prev.val)
                temp = temp.next
                n = n - 1
            # print(temp.val)
            # new relation
            temp.next = temp.next.next

        # while prev:
        #     print(prev.val)
        #     prev = prev.next
        # reverse the linkdlist
        prev, cur = None, prev
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # print(prev.val)
        return prev