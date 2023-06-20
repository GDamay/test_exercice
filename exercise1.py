def fibonacci(n: int) -> int:
    """Compute the fibonacci sequence of index n

    Parameters
    ----------
    n : int
        index of the fibonacci number to compute

    Returns
    -------
    int
        the n th number of the fibonacci sequence
    """

    if(n<=2):
        return 1
    else:
        return fib(n-1) + fib(n-2)
