import random
import quicksort

def randomizedpartition(A, p, r):
    i = random.randrange(p, r)   
    quicksort.exchange(A, i, r)
    return quicksort.partition(A, p, r)

def randomizedquicksort(A, p, r):
    """
    >>> A = [2, 8, 7, 1, 3, 5, 6, 4]
    >>> randomizedquicksort(A, 0, 7)
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    if p < r:
        q = randomizedpartition(A, p, r)
        randomizedquicksort(A, p, q - 1)
        randomizedquicksort(A, q + 1, r)
    return A

if __name__ == '__main__':
    from filetolist import argstolist
    lines = argstolist(int)

    print lines
    print randomizedquicksort(lines, 0, len(lines)-1)
