#1:
def greet(name):
    """
     Create a function called greet that takes a name as an argument and prints "Hello, [name]!".

    Args:
        name (str): The name of the person to greet.
    """
    print(f'Hello, {name}!')

#2: 
def goldilocks(size):
    """

    Create a function called goldilocks that takes a size as an argument. If the size is less than 140, print "Too small!". If the size is greater than 150, print "Too large!". Otherwise, print "Just right. :)".

    Args:
        size (int): The size to evaluate.
    """
    if (size<140):
        print('Too small!')
        
    elif (size>150):
        print('Too large!')
    else:
        print('Just right. :)')

#3
def square_list(numbers):
    """
    Create a function called square_list that takes a list of numbers and prints a list of their squares.

    Args:
        numbers (list): A list of numbers to be squared.
    """
    print([number**2 for number in numbers])

#4
def fibonacci_stop(max_value):

    """
    Generate and print a Fibonacci sequence up to a maximum value.

    Args:
        max_value (int): The maximum value for the Fibonacci sequence.
    """
    fib_seq = [1,1]
    while fib_seq[-1]+fib_seq[-2] <=max_value:
        fib_seq.append(fib_seq[-1]+fib_seq[-2])
    print(fib_seq)

#5
def clean_pitch(measurements, status):
    """
    Clean the pitch measurements by setting invalid measurements to -999.

    Args:
        measurements (list of int): A list of pitch measurements.
        status (list of int): A list of status signals corresponding to the measurements.
    """
    for i, (measurement,signal) in enumerate(zip(measurements,status)):
        if (measurement> 90 or measurement<0) and signal ==1:
            measurements[i] = -999
    
    print(measurements)
