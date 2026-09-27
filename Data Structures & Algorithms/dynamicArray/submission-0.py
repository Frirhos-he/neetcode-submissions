class DynamicArray:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError(
                f"{self.__class__.__name__} cannot be initialized with capacity {capacity}"
            )

        self.array = [None] * capacity
        self.current_index = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.current_index == len(self.array):
            self.resize()

        self.array[self.current_index] = n
        self.current_index += 1

    def popback(self) -> int:
        self.current_index -= 1
        value = self.array[self.current_index]
        self.array[self.current_index] = None
        return value

    def resize(self) -> None:
        tmp = [None] * (len(self.array) * 2)

        for i in range(len(self.array)):
            tmp[i] = self.array[i]

        self.array = tmp

    def getSize(self) -> int:
        return self.current_index

    def getCapacity(self) -> int:
        return len(self.array)