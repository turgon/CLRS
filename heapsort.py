def parent(i):
    """
    Get the parent index of i
    >>> parent(1)
    0
    >>> parent(2)
    1
    >>> parent(3)
    1
    >>> parent(4)
    2
    """
    return i >> 1

def left(i):
    """
    Get the index of the ith node's left child
    >>> left(1)
    2
    >>> left(2)
    4
    >>> left(3)
    6
    """
    return i << 1

def right(i):
    """
    Get the index of the ith node's right child
    >>> right(1)
    3
    >>> right(2)
    5
    >>> right(3)
    7
    """
    return (i << 1) + 1

class Heap:
    """
    Note: this is a lot easier when array indices start with 1 rather than 0.
    Fortunately I need a place to store heap_size, so I'll do so in A[0].
    That means A[1] is the max value in the heap.
    """
    
    def __init__(self, initial=[]):
        self.heap_size = 0
        self.A = [0]
        self.A[1:] = initial
        self.A = self.build_max_heap()

    def max_heapify(self, i):
        """
        I make the assumption that the ith node's left and right children are
        both max heaps.  Then, this function enforces the heap property on
        A at the ith node.
        >>> a = Heap([1])
        >>> a.max_heapify(1)
        [1]
        >>> a = Heap([1, 2, 1])
        >>> a.max_heapify(1)
        [2, 1, 1]
        >>> a = Heap([1, 1, 2])
        >>> a.max_heapify(1)
        [2, 1, 1]
        >>> a = Heap([1, 2, 1, 2, 1])
        >>> a.max_heapify(1)
        [2, 2, 1, 1, 1]
        """
        l = left(i)
        r = right(i)
        s = self.heap_size

        if l <= s and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i

        if r <= s and self.A[r] > self.A[largest]:
            largest = r

        if largest != i:
            tmp = self.A[i]
            self.A[i] = self.A[largest]
            self.A[largest] = tmp
            self.max_heapify(largest)

        return self.A[1:]

    def build_max_heap(self):
        """
        I suppose that A is an unordered heap, i.e.: A[0] is a dead placeholder.
        >>> a = Heap([1, 2, 3])
        >>> print a.A
        [0, 3, 2, 1]
        >>> a = Heap([1, 2, 3, 4, 5, 6, 7, 8])
        >>> print a.A
        [0, 8, 5, 7, 4, 1, 6, 3, 2]
        """

        self.heap_size = len(self.A) - 1

        for i in xrange(self.heap_size/2, 0, -1):
            self.max_heapify(i)

        return self.A

    def heapsort(self):
        """
        >>> a = Heap([1, 2, 3, 4, 5])
        >>> a.heapsort()
        [1, 2, 3, 4, 5]
        >>> a = Heap([2, 1, 4, 3, 6, 5, 8, 7, 9])
        >>> a.heapsort()
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        """

        self.build_max_heap()
        for i in xrange(len(self.A)-1, 1, -1):
            tmp = self.A[1]
            self.A[1] = self.A[i]
            self.A[i] = tmp
            self.heap_size = self.heap_size - 1
            self.max_heapify(1)

        return self.A[1:]

if __name__ == '__main__':
    from filetolist import argstolist
    lines = argstolist(int)

    lines.insert(0, 0) 

    print lines
    a = Heap(lines)
    print a.heapsort()
