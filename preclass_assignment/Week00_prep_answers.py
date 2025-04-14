#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:16:19 2025

@author: josephabbott
"""

#simple function

def greet(name: str) -> None:
    print(f"Hello, {name}!")

greet('World')
#%% if else statement 

def goldilocks(bed_length: int) -> None:
    if bed_length < 140:
        print("Too small!")
    elif bed_length > 150:
        print("Too large!")
    else:
        print("Just right. :)")
        
goldilocks(139)
goldilocks(140)
goldilocks(145)
goldilocks(150)
goldilocks(151)

#%% Lists 

def square_list(numbers: list) -> list:     #returning list 
    squared_numbers = []                    #initializing the list 
    for num in numbers:                     #The loop over function is the num 
        squared_numbers.append(num ** 2)    #adding the numbers from the loop 
    return squared_numbers                  

square_list([1,2,3,4])
#%%

def fibonacci_stop(max_value: int) -> list:
    fibonacci_sequence = [1, 1]                                     # Start with the first two Fibonacci numbers
    while True:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Sum of last two numbers
        if next_fib > max_value:
            break                                                   # Stop if the next Fibonacci number exceeds max_value
        fibonacci_sequence.append(next_fib)
    return fibonacci_sequence



#%%

def clean_pitch(pitch_angles: list, status_signals: list) -> list:
    cleaned_data = []
    
    for pitch, status in zip(pitch_angles, status_signals):
        if (pitch < 0 or pitch > 90) and status > 0:
            cleaned_data.append(-999)                               # Set bad values to -999
        else:
            cleaned_data.append(pitch)                              # Keep good values unchanged
    
    return cleaned_data

x = [-1, 100, 6, 95]  # "raw" pitch angle at four time steps
status = [1, 1, 0, 0]  # status signal

