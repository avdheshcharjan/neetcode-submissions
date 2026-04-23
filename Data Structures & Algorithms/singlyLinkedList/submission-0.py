class LinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
    
    def __init__(self):
        self.head= None
        self.tail = None

    def get(self, index: int) -> int:
        current = self.head
        count =0
        while current:
            if count == index:
                return current.val
            current=current.next
            count+=1

        return -1
        

    def insertHead(self, val: int) -> None:
        new_node=self.Node(val) #create a new node with some val
        new_node.next=self.head
        # Node0.val=head #rubbish
        self.head=new_node

        if self.tail is None:
            self.tail = new_node #empty case handling

    def insertTail(self, val: int) -> None:
        new_node = self.Node(val)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node

        self.tail.next=new_node
        self.tail=new_node

        if self.head is None:
            self.head = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        
        if index==0:
            self.head=self.head.next

            if self.head is None:
                self.tail=None
            return True
        
        current = self.head
        counter = 0

        while current and counter < index -1:
            current=current.next
            counter+=1
        
        # Out of bounds
        if current is None or current.next is None:
            return False

        # Remove node
        if current.next == self.tail:
            self.tail = current

        current.next = current.next.next
        return True



    def getValues(self) -> List[int]:
        values = []
        current=self.head

        while current:
            values.append(current.val)
            current=current.next
        return values




