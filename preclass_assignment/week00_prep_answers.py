# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:00:02 2025

@author: annat
"""

#%% 1. Define a function called greet that takes a name as a string, then prints "Hello, <name>!" to the screen.

def greet(x):
    return print("Hello, " + x + "!")

greet("world")

#%% 2. Goldilocks is 135 cm tall, and she is very picky about the size of her bed. If the bed is shorter than 140 cm, or larger than 150 cm, then she is unhappy. Write a function called goldilocks that takes the length of a bed in cm and prints whether goldilocks is happy with it. Be sure to distinguish whether the bed is too small or too large!

def goldilocks(x):
    if x < 140:
        mood = "Too small!"
    if x > 150:
        mood = "Too large!"
    if 140 <= x <= 150:
        mood = "Just right!"
    return print(mood)

goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

#%% 3. Write a function called square_list that takes a list of numbers and returns a list where each element has been squared.

def square_list(numbers):
    squared = []
    for x in numbers:
        squared.append(x**2)
    print(squared)
    
square_list([1,2,3])
    
#%% 4. Write a function called fibonacci_stop that returns a list of the Fibonacci numbers up to a specified maximum value. Recall that the Fibonacci sequence is a sequence in which the next number is the sum of the previous two numbers: 1, 1, 2, 3, 5, etc.

def fibonacci_stop(max):
        
    if max < 1: #returns empty if max value is less than 1.
        return []
    
    fibonacci = [1,1]
    
    next = fibonacci[-1] + fibonacci [-2] 
    while next <= max:
        fibonacci.append(next)
        next = fibonacci[-1] + fibonacci[-2]

    return fibonacci
    
fibonacci_stop(30)

#%% 5. Logical operators

def clean_pitch(x, status):
    
    clean_pitch_angles = []
    
    for angle, stat in zip(x,status): 
        if(angle < 0 or angle > 90) and stat > 0:
            clean_pitch_angles.append(-999)
        else:
            clean_pitch_angles.append(angle)
   
    return clean_pitch_angles

# Test
x = [-1,2,6,95]
status = [1,0,0,0]

print(clean_pitch(x,status))







