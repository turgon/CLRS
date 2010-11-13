
def merge(A, p, q, r):
    """
    Assumes A[p:q] and A[q:r+1] are both sorted, and that
    p <= q < r for p,q,r indices of A

    >>> merge([1,2,3,1,2,3], 0, 2, 5)
    [1, 1, 2, 2, 3, 3]

    """
    L = A[p:q+1]
    R = A[q+1:r+1]
    i = 0
    j = 0

    for k in xrange(p, r+1):
        try:
            L[i]
        except IndexError:
            A[k:r+1] = R[j:]
            return A

        try:
            R[j]
        except IndexError:
            A[k:r+1] = L[i:]
            return A

        if L[i] <= R[j]:
            # The top ofthe stack of L is at least as small as that of R, so use it.
            A[k] = L[i]
            i = i + 1

        else:
            # Otherwise, we must use the top of the stack of R.
            A[k] = R[j]
            j = j + 1

    return A

def mergesort(A, p, r):
    """
    A must be a list s.t. p <= r for p,r indices of A

    >>> mergesort([1,3,2,4,6,5,8,7], 0, 7)
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    if p < r:
        q = (p + r) / 2  # let integer division work its magic
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)
    
    return A

if __name__ == '__main__':
    from filetolist import argstolist
    lines = argstolist(int)

    print lines
    print mergesort(lines, 0, len(lines)-1)
