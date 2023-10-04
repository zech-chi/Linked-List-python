class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1001)]

    def put(self, key: int, value: int) -> None:
        node = self.map[key % 1001]
        while (node.next):
            if node.next.key == key:
                node.next.value = value
                return
            node = node.next
        if node.key == key:
            node.value = value
        else:
            node.next = ListNode(key, value) 

    def get(self, key: int) -> int:
        node = self.map[key % 1001]
        while (node):
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        node = self.map[key % 1001]
        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
