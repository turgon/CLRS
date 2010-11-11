"""
This POS is O(n^2)
"""
def insertion_sort(A):
    """
    >>> insertion_sort([4,3,2,1,0])
    [0, 1, 2, 3, 4]
    >>> insertion_sort([4])
    [4]
    """
    if len(A) == 1:
        return A
    for j in xrange(1, len(A)): # skip 0th
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key: # include 0th i
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

    return A

if __name__ == '__main__':
    lines = []

    from optparse import OptionParser
    parser = OptionParser()
    (options, args) = parser.parse_args()

    for f in args:
        try:
            fh = open(f, "r")
        except:
            parser.error("Unable to load %s" % f)

        try:
            fl = [int(x) for x in fh.readlines()]
        except:
            parser.error("Unable to read %s" % f)

        lines.extend(fl)

    print lines
    print insertion_sort(lines)
