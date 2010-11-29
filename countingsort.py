def countingsort(A):
    """
    >>> countingsort([2, 5, 3, 0, 2, 3, 0, 3])
    [0, 0, 2, 2, 3, 3, 3, 5]
    """
    # Get this max value in the list in O(n)
    k = max(A)

    # Initialize C
    C = [ 0 for i in xrange(0, k+1) ]

    # Populate C with the number of elements in A with value of C's indexes
    for j in xrange(0, len(A)):
        C[A[j]] = C[A[j]] + 1

    # Now convert C to running sums
    for i in xrange(1, k+1):
        C[i] = C[i] + C[i-1]

    # Finally, sort to B
    B = [ 0 for j in xrange(0, len(A)) ]
    for j in xrange(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1
    
    return B

if __name__ == '__main__':
    from filetolist import argstolist
    lines = argstolist(int)

    print lines
    print countingsort(lines)
