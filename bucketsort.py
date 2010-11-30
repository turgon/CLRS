import insertion_sort

def bucketsort(A):
    """
    A must be a list of floats s.t. for all x in A, 0 <= x < 1
    >>> bucketsort([0.1, 0.2])
    [0.10000000000000001, 0.20000000000000001]
    >>> bucketsort([0.2, 0.1])
    [0.10000000000000001, 0.20000000000000001]
    >>> bucketsort([])
    []
    """
    n = len(A)
    B = [[] for j in range(0, n)]
    C = []
    for i in xrange(0, n):
        j = int(n*A[i])
        B[j].append(A[i])
    for b in B:
        insertion_sort.insertion_sort(b)
        C = C + b
    return C

if __name__ == '__main__':
    from filetolist import argstolist
    lines = argstolist(float)

    print lines
    print bucketsort(lines)
