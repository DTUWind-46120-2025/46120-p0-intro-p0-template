from numpy import *;

### Ex. 1
def greet(name):
    print(f'Hello {name}!')

greet('Lara')

### Ex. 2
def goldilocks(length):
    if length < 140:
        print('Too small!')
    elif length > 150:
        print('Too large!')
    else:
        print('Perfect!')

goldilocks(130)
goldilocks(145)
goldilocks(160)

### Ex.3
def square_list(array):
    for i in range(len(array)):  
        array[i] = array[i] ** 2  

    return array  

print(square_list([1, 2, 3, 4, 7, 8]))  

### Ex. 4
def fibonacci_stop(max):
    array = [0, 1]
    while array[-1] + array[-2] < max:
        array.append(array[-1] + array[-2])
    return array
print(fibonacci_stop(60))

### Ex. 5

def clean_pitch(x, status):
    for i in range(len(x)):
        if status[i] == True:
            x[i] = -999
    return x

print(clean_pitch([1, 5, 67, 91, 34, 120], [0, 0, 0, 0, 1, 1]))        
        