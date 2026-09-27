
class Node:
    def __init__(self, val: int, next: Node = None) -> None:
        self.val:int = val
        self.next:Node|None = next
    

class LinkedList:
    
    def __init__(self):
        self.head: Node|None = None
        self.size = 0

    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        tmp = self.head
        counter = 0
        while tmp != None and counter != index:
            tmp = tmp.next
            counter += 1
        return tmp.val

    def insertHead(self, val: int) -> None:
        tmp = Node(val, self.head)
        self.head = tmp
        self.size+=1        

    def insertTail(self, val: int) -> None:
        self.size+=1
        if self.head is None:
            self.head = Node(val)
            return
        tmp = self.head
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = Node(val)
        return

    def remove(self, index: int) -> bool:
        if index< 0 or self.size <= index:
            return False
        if index == 0:
            if self.head:
                self.head = self.head.next
                self.size -= 1
                return True
            return False

        counter = 0
        prev = self.head
        while counter!= (index - 1) and prev.next != None:
            counter+=1
            prev = prev.next
        
        curr = prev.next
        if curr:
            prev.next = curr.next
            curr.next = None
            curr = None
        self.size -= 1
        return True



    def getValues(self) -> List[int]:
        values = []
        tmp = self.head
        while tmp != None:
            values.append(tmp.val)
            tmp = tmp.next
        return values        
