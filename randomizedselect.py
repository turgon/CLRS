from randomizedquicksort import randomizedpartition

def randomizedselect(A, p, r, i):
    """
    Returns the ith smallest element of the subarray A[p:r+1]
    >>> randomizedselect([0, 1, 2, 3], 0, 3, 1)
    0
    >>> randomizedselect([0, 1, 2, 3], 0, 3, 2)
    1
    >>> randomizedselect([0, 1, 2, 3], 0, 3, 3)
    2
    >>> randomizedselect([0, 1, 2, 3], 0, 3, 4)
    3
    >>> randomizedselect([2, 3, 0, 1], 0, 3, 1)
    0
    >>> randomizedselect([2, 3, 0, 1], 0, 3, 2)
    1
    >>> randomizedselect([2, 3, 0, 1], 0, 3, 3)
    2
    >>> randomizedselect([2, 3, 0, 1], 0, 3, 4)
    3
    """
    if p == r:
        return A[p]
    q = randomizedpartition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomizedselect(A, p, q-1, i)
    else:
        return randomizedselect(A, q+1, r, i - k)

if __name__ == '__main__':
    from filetolist import argstolist
    lines = argstolist(int)

    print lines
    print randomizedselect(lines, 0, len(lines)-1, 50000)
