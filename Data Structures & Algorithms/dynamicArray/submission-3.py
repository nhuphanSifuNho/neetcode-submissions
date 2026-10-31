class DynamicArray:
    
    def __init__(self, capacity: int):
        # 1. Store the initial capacity
        self.capacity = capacity # stores the maximum number of elms the array can hold
        # 2. Initialize the size 
        self.size = 0  # the arrays starts empty
        # 3. Create the underlying storage
        self.arr = [0] * capacity # allows capacity slots, initialized to 0
        

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        # 1. Check whether the array is full
        if self.size == self.capacity:

        # 2. If full, call resize()
            self.resize()

        # 3. Insert n at the correct index
        self.arr[self.size] = n

        # 4. Update size
        self.size += 1


    def popback(self) -> int:
        # 1. Decrease size
        self.size -= 1

        # 2. Return the last valid element
        return self.arr[self.size]

 

    def resize(self) -> None:
        # 1. Double self.capacity
        self.capacity *= 2

        # 2. Create a new list with the updated capacity
        new_arr = [0] * self.capacity

        # 3. Copy all existing elements from self.arr into the new list
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        
        # 4. Replace the old array with the new array
        self.arr = new_arr



    def getSize(self) -> int:
        # What attribute stores the number of elements currently in the array?
        return self.size
        
    
    def getCapacity(self) -> int:
        # What attributes stores the total available slots?
        return self.capacity

