def fibonacci_number(offset, n):
    """ Return a sequence of number which is selected from the fibonacci 
    sequence which the 3th number is eliminated then added a offset. 

    >>> list(fibMonaccian(0, 0))
    []
    """

    t2 = 1
    t1 = 1
    t = 2

    if n > offset:
        yield offset, -1
        if n > 1+offset:
            yield 1+offset, offset
            while t+offset < n:
                yield t+offset, t1+offset
                t, t1, t2 = t+t1, t, t1


def index(arr, x):
    """Fibonacci search

    """
    n = len(arr)
    point_start = 0
    point_stop = n

    while point_stop > point_start:
        for t, t1 in fibonacci_number(point_start, point_stop):
            if arr[t] == x:
                return t
            elif arr[t] > x:
                if t1 == -1:
                    return -1
                point_start = t1+1
                point_stop = t
                break
        else:
            point_start = t+1

    return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
