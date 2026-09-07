# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is not None and list2 is not None:
            if list1.val > list2.val:
                v = list2.val
                list2 = list2.next
            else:
                v = list1.val
                list1 = list1.next

        elif list1 is not None:
            v = list1.val
            list1 = list1.next
        elif list2 is not None:
            v = list2.val
            list2 = list2.next
        else:
            return None


        head = ListNode(v)
        cur = head
        # print(list1.val)
        while(list1 and list2):
            v1 = list1.val
            v2 = list2.val
            if(v1 > v2):
                node = ListNode(v2)
                cur.next = node
                cur = cur.next
                list2 = list2.next
            else:
                node = ListNode(v1)
                cur.next = node
                cur = cur.next
                list1 = list1.next
                
        while(list1 != None):
            v = list1.val
            node = ListNode(v)
            cur.next = node
            cur = cur.next
            list1 = list1.next

        while(list2 != None):
            v = list2.val
            node = ListNode(v)
            cur.next = node
            cur = cur.next
            list2 = list2.next

        return head
        