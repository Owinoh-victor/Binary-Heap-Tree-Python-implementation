class BinaryHeap:
    def __init__(self):
        self.heap = []
    def left_child(self, i):
        return 2*i + 1    
    def right_child(self, i):
        return 2*i + 2
     
    def Length(self):
        return len(self.heap)
 
    def Parent(self, i):
        return (i - 1)//2
    
    def Get_Index(self, i):
        return self.heap[i]
 
    def get_max(self):
        if self.Length() == 0:
            return None
        return self.heap[0]
 
    def Extract_maximum(self):
        if self.Length() == 0:
            return None
        largest = self.get_max()
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.max_heapify(0)
        return largest
 
    def max_heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        if (l <= self.Length() - 1 and self.Get_Index(l) > self.Get_Index(i)):
            largest = l
        else:
            largest = i
        if (r <= self.Length() - 1 and self.Get_Index(r) > self.Get_Index(largest)):
            largest = r
        if (largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)
 
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
 
    def Insert_data(self, key):
        index = self.Length()
        self.heap.append(key)
 
        while (index != 0):
            p = self.Parent(index)
            if self.Get_Index(p) < self.Get_Index(index):
                self.swap(p, index)
            index = p
 
 
heap = BinaryHeap()
print('Insert Element')
print('max get')
print('max extract')
print('quit')
 
while True:
    option = input('Enter the choice').split()
 
    choice = option[0].strip().lower()
    if choice == 'Insert Element':
        data = int(option[1])
        heap.Insert_data(data)
    elif choice == 'max':
        suboperation = option[1].strip().lower()
        if suboperation == 'get':
            print('Maximum value: {}'.format(heap.get_max()))
        elif suboperation == 'extract':
            print('Maximum value removed: {}'.format(heap.Extract_maximum()))
 
    elif choice == 'quit':
    break
