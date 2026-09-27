class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Cannot instatiate an array with that capacity")
        self.array = [None] * capacity
        self.index = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        while i > len(self.array)-1:
            self.resize()
        self.array[i] = n
        if i > self.index:
            self.index = i

    def pushback(self, n: int) -> None:
        if self.index >= len(self.array):
            self.resize()
        self.array[self.index] = n 
        self.index = self.index + 1 

    def popback(self) -> int:
        result = self.array[self.index-1]
        self.array[self.index-1] = None
        self.index -= 1
        return result

    def resize(self) -> None:
        tmp = [None] * len(self.array)* 2
        tmp[:len(self.array)] = self.array
        self.array = tmp

    def getSize(self) -> int:
        return self.index
    
    def getCapacity(self) -> int:
        return len(self.array)