"""
Header: UW 2017 - Intro To Python
Topic: Fibonacci and Lucas Series
Author: PydPiper

Objective: Write a function for the Fib and Lucas series that returns the n'th item in the series.
            Fib: 0, 1, 1, 2, 3, 5, 8...
            (starts with 0, 1 then adds the past 2 to get the next)
            Lucas: 2, 1, 3, 4, 7, 11, 18...
            (same as fib but starts with 2, 1)
"""


def added_series(term1: int = 0, term2: int = 1, nth_term: int = 3) -> int:
    """
    A customizable function that can accept any term 1 and 2 to accomodate fib or lucas series
    Fibonacci series: 0, 1, 1, 2, 3, 5, 8...

    :param term1: (int, default=0) term 1 of the series
    :param term2: (int, default=1) term 2 of the series
    :param nth_term: (int > 0, default=3) input for desired n'th term return value
    :return: (int) return's the n'th term in the Series
    """

    if nth_term <= 0:
        raise ValueError("nth_term cannot be less than 1")

    # condition for term 1 and 2 call
    if nth_term == 1:
        return term1
    elif nth_term == 2:
        return term2

    # condition for term >= 3
    if nth_term == 3:
        # if current recursion hit the desired n'th term, add term1 and term2 and return it
        rv = term1 + term2
        return rv
    else:
        nth_term -= 1
        rv = term1 + term2
        try:
            rv = added_series(term1=term2, term2=rv, nth_term=nth_term)
        except RecursionError:
            raise RecursionError("RecursionError occurred, overwrite the default python recursion by:"
                                 "sys.setrecursionlimit(nth_term)")

    return rv


def fibonacci(nth_term: int = 3) -> int:
    """
    Fibonacci series: 0, 1, 1, 2, 3, 5, 8...

    :param nth_term: (int, default=3) input for desired n'th term return value
    :return: (int) return's the n'th term in the Series
    """

    return added_series(term1=0, term2=1, nth_term=nth_term)


def lucas(nth_term: int = 3) -> int:
    """
    Lucas series: 2, 1, 3, 4, 7, 11, 18...

    :param nth_term: (int, default=3) input for desired n'th term return value
    :return: (int) return's the n'th term in the Series
    """

    return added_series(term1=2, term2=1, nth_term=nth_term)


if __name__ == "__main__":
    print("Fib Series 6th term: ", fibonacci(7))
    print("Lucas Series 6th term: ", lucas(7))
