class ListNode:
    def __init__(self,  val=0, key=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
        



class LRUCache:

    def __init__(self, capacity: int):
        self.lrumap = {}
        self.capacity = capacity
         # Dummy nodes
        self.head = ListNode()  
        self.tail = ListNode()  

        self.head.next = self.tail
        self.tail.prev = self.head
        # self.prev = prev


    # change position(can be tail node), new node, 
    def insert_at_head(self, node, isNew=False):
        if isNew:
            headNext = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = headNext
            headNext.prev = node

            # node.next = self.head
            # self.head.prev = node
            # self.head = node
            self.capacity -= 1


        else:
            prev = node.prev
            prev.next = node.next
            node.next.prev = prev

            headNext = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = headNext
            headNext.prev = node
            # self.capacity -= 1


    def remove(self):
        # can be the last one, or head and tail is the same one
        del self.lrumap[self.tail.prev.key]
        
        prev = self.tail.prev.prev
        prev.next = self.tail
        self.tail.prev = prev
        self.capacity += 1

    def get(self, key: int) -> int:
        node = self.lrumap.get(key)
        if node:
            self.insert_at_head(node)
            return node.val
        else: 
            return -1



    def put(self, key: int, value: int) -> None:
        # Update
        if self.lrumap.get(key):
            self.lrumap[key].val = value
            self.insert_at_head(self.lrumap.get(key))


        # Create new one, and handel self.capacity
        else:
            if not self.capacity:
                self.remove()
                newNode = ListNode(value, key)
            
                self.insert_at_head(newNode, True)
                self.lrumap[key] = newNode
            else:
                newNode = ListNode(value, key)
            
                self.insert_at_head(newNode, True)
                self.lrumap[key] = newNode

