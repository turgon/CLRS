def hornersrule(coeff, x):
    """
    Horner's Rule is a simple optimization of polynomial evaluation,
    following the form:
    
        y = a0 + x(a1 + x(a2 + ... + x(a_(n-1) + x*an)...)

    Test the equivalent of a 16-bit integer with all bits flipped
    >>> hornersrule([1 for i in range(0, 16)], 2)
    65535
    """
    y = 0
    for i in xrange(len(coeff)-1, -1, -1):
        y = coeff[i] + x*y

    return y

if __name__ == '__main__':
    from filetolist import argstolist
    lines = argstolist(float)

    # Assume the first is x
    x = lines[0]
    lines = lines[1:]

    print x, lines
    print hornersrule(lines, x)
