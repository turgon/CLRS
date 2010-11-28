def exchange(A, i, j):
    """
    Swap the ith and jth elements in A
    >>> A = [1, 2]
    >>> exchange(A, 0, 1)
    >>> A
    [2, 1]
    """
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def partition(A, p, r):
    """
    Partition the array s.t. the last element becomes the pivot,
    for which all elements of lesser value occur ealier in the array,
    and all elements with greater value occur later than the pivot.
    >>> A = [2, 8, 7, 1, 3, 5, 6, 4]
    >>> partition(A, 0, 7)
    3
    >>> A
    [2, 1, 3, 4, 7, 5, 6, 8]
    """
    x = A[r]
    i = p - 1
    for j in xrange(p, r):
        if A[j] <= x:
            i = i + 1
            exchange(A, i, j)
    q = i + 1
    exchange(A, q, r)
    return q

def quicksort(A, p, r):
    """
    >>> A = [2, 8, 7, 1, 3, 5, 6, 4]
    >>> quicksort(A, 0, 7)
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)
    return A

if __name__ == '__main__':
    from filetolist import argstolist
    lines = argstolist(int)

    print lines
    print quicksort(lines, 0, len(lines)-1)
