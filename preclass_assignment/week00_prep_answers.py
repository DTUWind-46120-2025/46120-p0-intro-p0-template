###Exercies for week 0 in PiWE

#Ex 1
def greet(name):
    """Returns in terminal a greet to the given name"""
    return print(f"Hello, {name}!")

#Ex 2
def goldilocks(bed_size):
    """define if the bed_size is good for goldilocks standarts"""
    if bed_size < 140:
        print("Too small!")
    if bed_size > 150:
        print("Too large!")
    else:
        print("Just right. :)")

#Ex 3
def square_list(list):
    """Takes in a list a give back a list with each element squared"""
    new_list=[]
    for i in list:
        new_list.append(i**2)
    return new_list

#Ex 4
def fibonacci_stop(max_val):
    """give the element of the fibonacci sequence lower that the max_val"""
    fib_list = []
    i = 1
    if max_val < 1:
        return fib_list
    fib_list.extend([1,1])
    i = 2
    while i < max_val:
        fib_list.append(i)
        i = fib_list[-2] + fib_list [-1]
        
    return fib_list

#Ex 5
def clean_pich(measurement, status):
    """Clean the measurement depending on the status signal list"""

    if len(measurement)!=len(status):
        raise Exception("Not the same lenght of signal !")
    
    empty_measurement = measurement[:]

    for i in range(len(measurement)):
        if status[i] == 1:
            empty_measurement[i] = -999
    return empty_measurement


    
