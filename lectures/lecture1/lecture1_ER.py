"""
Part 2, Lecture 1

Implement and test an argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns
    the index (position) of the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an
    empty sequence.

4.  Use the notebook lecture1.ipynb to benchmark your implementation
    against NumPy's argmax().

"""

import numpy as np


def argmax(values):
    """
    Return the index of the maximum value in a collect.

    Parameters
    ----------
    values
       sequence of values
    returns
    -------
    imax:int
        index of the maximum value in values

    """
    N = len(values)

    imax = None
    vmax = -np.inf
    for i in range(N):
        # first iteration: value = 2
        value = values[i]
        # check whether value is larger than any previous
        if value > vmax:
            # update the index and the vmax
            imax = i
            vmax = value

    return imax


values = [2, 3, -1, 7, 4]

imax = argmax(values)

print(f'the imax values is at {imax}')

easy = np.argmax(values)
print(easy)

values = []

#compare to numpy argmax
