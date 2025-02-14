
import numpy as np
import pandas as pd
import scipy as sci
import matplotlib.pyplot as plt

# 1. Write a simple function
def greet(name):
    """This functions prints 'Hello, keyword'.
    
    input:
        name {str}
    output:
        None"""
    
    print(f"Hello, {name}!")
    return

# 2. If/else statements
def goldilocks(bed_size):
    """This function should check whether the bed of the size
      given by the keyword fits Goldilocks' demands.
    
    input:
        bed_size {int/float} 
    output:
        None"""
    
    # goldilocks_height = 135 # [cm]
    if bed_size < 140: # [cm]
        return print("Too small!")
    elif bed_size > 150: # [cm]
        return print("Too large!")
    else:
        return print("Just right. :)")


# 3. For loops
def square_list(l):
    """This function takes a list as input and squares all 
    elements separately.
    
    input:
        l {list:int/float}
    output:
        l_ {list:int/float}"""
    
    l_ = l.copy()
    for idx in range(len(l)):
        l_[idx] = l[idx]**2
    return l_

# 4. While loops
def fibonacci_stop(max_val):
    """This function takes a single value as input and gives 
    the highest value of the Fibonacci sequence, before reaching 
    this number.

    input:
        max_val {int/float} 
    output:
        fibonacci_sequence[:-1] {list:int/float}"""
    
    fibonacci_sequence = []
    fibonacci_sequence.append(1)
    while fibonacci_sequence[-1] < max_val:
        fibonacci_sequence.append(sum(fibonacci_sequence[-2:]))
    return fibonacci_sequence[:-1]

#5. Logical operators
def clean_pitch(x,status):
    """This function takes as input the pitch signal x and 
    a status signal (both for a wind turbine). And then it returns
    'bad' pitch angles are set to -999 and 'good' values are simply returned.
    The 'bad' angles have a status signal of '1'.

    input:
        x {list:int/float}
        status {list:int}
    output:
        x_ {list:int/float}"""
    
    x_ = x.copy()
    for idx in range(len(x)):
        if status[idx] == 0:
            x_[idx] = x[idx]
        else:
            x_[idx] = -999
    return x_

# This is just there to show the functionality of the if-statement below.
if __name__ == "__main__":
    print("This is the functions file, it shouldn't be run directly!")