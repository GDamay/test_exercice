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
        return fibonacci(n-1) + fibonacci(n-2)
