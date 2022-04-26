class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.size = 0
        self.head = None # dummy head node

    def add(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        new_node = Node(data)
        cur.next = new_node
        self.size += 1

    def insert(self, i:int, data):
        prev_node = self.head
        cur_node = prev_node.next

        for _ in range(i):
            prev_node = prev_node.next
            cur_node = cur_node.next

        new_node = Node(data)
        prev_node.next = new_node
        new_node.next = cur_node
        self.size += 1

    def clear(self):
        self.size = 0
        self.head.next = None
    
    def delete(self, t) -> bool:
        pass

    def deleteByIndex(self, i:int) -> bool:
        pass

    def get(self, i:int):
        pass

    def indexOf(self, t):
        pass

    def isEmpty(self) -> bool:
        pass

    def contains(self, t) -> bool:
        pass

    def size(self) -> int:
        pass
