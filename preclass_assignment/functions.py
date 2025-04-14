import numpy as np      #Importing the packages


def greet(name):        #Defining the function
    print('Hello,',name+'!') #Combining it to a single string, and printing it


def goldilocks(bedsize):      #Defining the function
    if bedsize > 150:   #A check to see if the bed is to big
        print('The bed was to big, Goldilocks was not happy!!')   #Text printet in a scenario where the bed is to big
    elif bedsize < 140:     #A check to see if the bed is to small
        print('The bed was to small, Goldilocks was not happy!!') #Text printet in a scenario where the bed is to samll
    else:       #If not to big or to small, the size must be perfect
        print('Goldilocks was happy, and would have extented her gratitude, if she was not slepping already.')  #Text printet in a scenario where the bed is perfect


def square_list(numbers): #Defining the function
    print(np.square(numbers)) #Squaring the numbers


def fibonacci_stop(number): #Defining the function
    array = ([None])*(number + 2)     #Making an empty list the size of the input numer + 2 (it's way bigger than it needs, at bigger inputs, which could be polished)
    fibonacci_new = 1   #Defining the newest fibonacci number
    fibonacci_old = 0   #Defining the oldest fibonacci number
    count = 1           #Defining a counter
    while fibonacci_new <= number:      #Making a while loop that runs undtil the new fibonacci number is bigger than the inputnumber
        array[0] = 1                    #Difining the first fibonacci number
        array[count] = fibonacci_new + fibonacci_old        #Difining the fibonacci numbers
        fibonacci_old = fibonacci_new                       #Changing the new number to the old
        fibonacci_new = array[count]                        #Defining the new new fibonacci number
        count += 1                      #Counting
    
    fibonacci_array = [item for item in array if item is not None]  #Removing all the excess empty values from the list
    del fibonacci_array[count-1]                                    #Deleting the last value in the list, as it has surpased the inputnumper
    print(fibonacci_array)              #Printing the fibonacci list


def clean_pitch(x,status):  #Defining the function

    for i in range(len(x)):     #Maling a for loop in the lengt of one of the input list
        if x[i] > 90 or x[i] < 0:   #Checking if the value in the list is out of the bounderies
            if status[i] > 0:       #Checking if the status showed a mistake
                x[i] = -999         #If both are true, change the value to -999 to show that something is wrong
    print(x)            #Print the new list of data