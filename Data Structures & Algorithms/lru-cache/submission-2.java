// import java.util.HashMap;

class LRUCache {

    class Node {
        int key, value;
        Node prev, next;
        public Node(int key, int value){
            this.key = key;
            this.value = value;
            this.prev =  null;
            this.next = null;
        }
    }

    private java.util.HashMap<Integer, Node> cache = new HashMap<>();
    private int capacity = 0;
    private int size = 0;
    private Node head = new Node(0, 0);
    private Node tail = new Node(0, 0);


    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.head.next = tail;
        this.tail.prev = this.head;
        
    }

    public void unlinkNode(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public void addToHead(Node node){
        node.next = head.next;
        node.next.prev = node;
        head.next = node;
        node.prev = head;
    }
    
    public int get(int key) {
        Node node = cache.get(key);
        if (node == null){
            return -1;
        }
        unlinkNode(node);
        addToHead(node);

        return node.value;
        
    }

    public void removeLruNode(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    public void put(int key, int value) {
        Node node = cache.get(key);
        if (node != null){
            node.value = value;
            unlinkNode(node);
            addToHead(node);
            return ;
        }
        
        if(size >= capacity){
            Node lruNode = tail.prev;
            removeLruNode(lruNode);
            cache.remove(lruNode.key);
            size --; 
        }
        Node newNode = new Node(key, value);
        addToHead(newNode);
        cache.put(key, newNode);
        size ++;
    }
}