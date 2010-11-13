def filetolist(path, mapper=None):
    """
    I take a file path and an optional mapper function reference.
    Each line in the file becomes an element in the returned list,
    optionally mapped through the mapper.
    """

    try:
        fh = open(path, "r")
    except:
        parser.error("Unable to load %s" % f)

    try:
        if mapper:
            fl = [mapper(x) for x in fh.readlines()]
        else:
            fl = [x for x in fh.readlines()]
    except:
        parser.error("Unable to read %s" % f)

    return fl

def filestolist(paths, mapper=None):
    """
    I take a list of paths and an optional mapper function,
    using filetolist() to create an extended list based on the contents
    of many files.
    """

    mylist = []

    for path in paths:
        mylist.extend(filetolist(path, mapper))

    return mylist

def argstolist(mapper=None):
    """
    I shortcut the assumption that a script might want to take an arbitrary
    list of files as arguments, read each into a list according to some map,
    and consume the list.
    """
    from optparse import OptionParser

    parser = OptionParser()
    (options, args) = parser.parse_args()

    return filestolist(args, mapper)    
