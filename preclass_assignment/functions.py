"""Functions for preclass assignment.
"""


def greet(name):
    """Print a greeting to someone."""
    print(f'Hello, {name}!')


def goldilocks(x):
    """Determine whether goldilocks is happy with the size of a bed (in cm)."""
    if x < 140:
        print('Too small!')
    elif x > 150:
        print('Too large!')
    else:
        print('Just right. :)')


def square_list(l):
    """Iterate through the elements of a list and square each one."""
    l2 = []
    for x in l:
        l2.append(x*x)
    return l2


def fibonacci_stop(x):
    """Return the fibonacci numbers below a maximum threshold."""
    f1 = 1  # initialize first number
    f2 = 1  # initialize second
    l = [f1]  # start list of numbers
    while f2 < x:  # stop when sequence is too large
        l.append(f2)  # append new number
        fo = f1 + f2  # calculate next step in sequence
        f1 = f2  # re-assign first number
        f2 = fo  # reassign second number
    return l


def clean_pitch(x, status):
    """Set all values outside 0 and 90 degrees to -999 if instrument is 
    malfunctioning (non-zero status)."""
    for i, x_i in enumerate(x):
        if ((x_i < 0) | (x_i > 90)) & (status[i]):
            x[i] = -999
    return x
