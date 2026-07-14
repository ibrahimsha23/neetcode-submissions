# class LRUCache:

#     def __init__(self, capacity: int):
        

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:
        

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node('head', 1)
        self.tail = Node('tail',0)
        self.memory_counter = {}
        self.counter = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def del_memory(self, k):
        del self.memory_counter[k]

    def add_to_memory(self, k, node):
        self.memory_counter[k] = node
        return None

    def link_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

        return

    def unlink_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


    def get(self, key):
        print(self.memory_counter)
        k = key
        if self.memory_counter.get(k):
            node = self.memory_counter[k]
            self.unlink_node(node)
            self.link_to_head(node)
            return node.val

        return -1


    def put(self, key, value):
        k, val = key, value

        if self.get(k) != -1:
            node = self.memory_counter[k]
            node.val = val
            return
        if len(self.memory_counter) >= self.capacity:
            lru_node = self.tail.prev
            self.unlink_node(lru_node)
            self.del_memory(lru_node.key)




        node = Node(k, val)
        self.add_to_memory(k, node)
        self.link_to_head(node)
        self.counter += 1

    def display(self):
        root = self.head.next
        counter = 0
        while root:
            counter += 1
            print(root.key, root.val, "counter---", counter)
            root = root.next
