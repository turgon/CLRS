from heapsort import Heap, parent

class HeapUnderflow(Exception):
    pass

class PriorityQueueIncreaseKeyFailure(Exception):
    pass

class PriorityQueue(Heap):
    
    def maximum(self):
        """
        Return the current heap maximum
        >>> a = PriorityQueue([1])
        >>> a.maximum()
        1
        >>> a = PriorityQueue([1, 2, 3, 4, 5])
        >>> a.maximum()
        5
        >>> a = PriorityQueue([2, 1, 9, 10, 0])
        >>> a.maximum()
        10
        """
        return self.A[1]

    def extract_max(self):
        """
        >>> a = PriorityQueue([])
        >>> a.extract_max()
        Traceback (most recent call last):
            ...
        HeapUnderflow
        >>> a = PriorityQueue([1, 2, 3, 4, 5])
        >>> a.extract_max()
        5
        >>> a.A
        [0, 4, 2, 3, 1]
        >>> a.extract_max()
        4
        >>> a.A
        [0, 3, 2, 1]
        >>> a.extract_max()
        3
        >>> a.A
        [0, 2, 1]
        >>> a.extract_max()
        2
        >>> a.A
        [0, 1]
        >>> a.extract_max()
        1
        >>> a.A
        [0]
        """
        if self.heap_size < 1:
            raise HeapUnderflow()
        m = self.A[1]
        self.A[1] = self.A[self.heap_size]
        self.heap_size = self.heap_size - 1
        self.max_heapify(1)
        self.A = self.A[:self.heap_size+1] # Fixes the internal array by clipping off the last element, which had been copied to the first.
        return m

    def increase_key(self, i, key, ignore_failure=False):
        """
        >>> a = PriorityQueue([1])
        >>> a.increase_key(1, 0)
        Traceback (most recent call last):
            ...
        PriorityQueueIncreaseKeyFailure: new key is smaller than old key: 0 < 1
        >>> a = PriorityQueue([1, 2, 3, 4, 5])
        >>> a.increase_key(5, 10)
        >>> a.A
        [0, 10, 5, 3, 1, 4]
        """
        if not ignore_failure and key < self.A[i]:
            raise PriorityQueueIncreaseKeyFailure("new key is smaller than old key: %s < %s" % (key, self.A[i]))
        self.A[i] = key
        p = parent(i)
        while i > 1 and self.A[p] < self.A[i]:
            tmp = self.A[p]
            self.A[p] = self.A[i]
            self.A[i] = tmp
            i = p
            p = parent(i)

    def insert_key(self, key):
        """
        >>> a = PriorityQueue([])
        >>> a.insert_key(10)
        >>> a.A
        [0, 10]
        """
        self.heap_size = self.heap_size + 1
        self.A.append(0)
        self.increase_key(self.heap_size, key, ignore_failure=True)
