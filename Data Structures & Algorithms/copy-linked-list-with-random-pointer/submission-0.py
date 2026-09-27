"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # iterating the linked list, create new node with a dictionary for storeing their pointer
        cur = head
        oldNewDic = {None: None}

        while cur:
            cpy = Node(cur.val)
            oldNewDic[cur] = cpy
            cur = cur.next



        cur = head
        while cur:
            cpy = oldNewDic[cur]
            cpy.next = oldNewDic[cur.next]
            cpy.random = oldNewDic[cur.random]
            cur = cur.next
        return oldNewDic[head]


