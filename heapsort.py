"""
Note: this is a lot easier when array indices start with 1 rather than 0.
Fortunately I need a place to store heap_size, so I'll do so in A[0].
That means A[1] is the max value in the heap.
"""

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

def heap_size(A):
    """
    Since as an implementation detail I have agreed to store the true heap
    size in A[0], I simply return that.
    >>> heap_size([0])
    0
    >>> heap_size([5])
    5
    """
    return A[0]

def max_heapify(A, i):
    """
    I make the assumption that the ith node's left and right children are
    both max heaps.  Then, this function enforces the heap property on
    A at the ith node.
    >>> max_heapify([1, 1], 1)
    [1, 1]
    >>> max_heapify([3, 1, 2, 1], 1)
    [3, 2, 1, 1]
    >>> max_heapify([3, 1, 1, 2], 1)
    [3, 2, 1, 1]
    >>> max_heapify([5, 1, 2, 1, 2, 1], 1)
    [5, 2, 2, 1, 1, 1]
    """
    l = left(i)
    r = right(i)
    s = heap_size(A)

    if l <= s and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= s and A[r] > A[largest]:
        largest = r

    if largest != i:
        tmp = A[i]
        A[i] = A[largest]
        A[largest] = tmp
        max_heapify(A, largest)

    return A

def build_max_heap(A):
    """
    I suppose that A is an unordered heap, i.e.: A[0] is a dead placeholder.
    >>> build_max_heap([0, 1, 2, 3])
    [3, 3, 2, 1]
    >>> build_max_heap([0, 1, 2, 3, 4, 5, 6, 7, 8])
    [8, 8, 5, 7, 4, 1, 6, 3, 2]
    """

    A[0] = len(A) - 1

    for i in xrange(A[0]/2, 0, -1):
        max_heapify(A, i)

    return A

def heapsort(A):
    """
    >>> heapsort([0, 1, 2, 3, 4, 5])
    [1, 1, 2, 3, 4, 5]
    >>> heapsort([0, 2, 1, 4, 3, 6, 5, 8, 7, 9])
    [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    build_max_heap(A)
    for i in xrange(len(A)-1, 1, -1):
        tmp = A[1]
        A[1] = A[i]
        A[i] = tmp
        A[0] = A[0] - 1
        max_heapify(A, 1)

    return A

if __name__ == '__main__':
    from filetolist import argstolist
    lines = argstolist(int)

    lines.insert(0, 0) 

    print lines
    print heapsort(lines)
