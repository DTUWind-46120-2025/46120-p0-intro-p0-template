
#%% EXERCISE 1

def printing_word(word):
    print('Hello,',word)

#%% EXERCISE 2
def length_bed(length):
    if length > 150:
        print('Too big!!')
    elif length < 140:
        print('Too small!!')
    else:
        print('Just right :)')

#%% EXERCISE 3
def square_list(numbers):
    squares = []
    for ii in range(0,len(numbers)):
        squares.append(numbers[ii]**2)
    return squares

#%% EXERCISE 4
def fibonacci_stop(maximum):
    series = [1, 1]
    while (series[-1]+series[-2])<= maximum:
        series.append(series[-1]+series[-2])
    return series

#%% EXERCISE 5
def clean_pitch(angles,status):
    correct_angles = angles.copy()
    for ii in range(0,len(angles)):
        if (angles[ii]<0 or angles[ii]>90) and status[ii] !=0:
            correct_angles[ii] = -999
    return correct_angles