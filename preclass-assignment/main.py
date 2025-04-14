from functions import *

if __name__ == '__main__':

    #1
    greet('world')

    #2
    goldilocks(139)
    goldilocks(140)
    goldilocks(151)
    goldilocks(150)

    #3
    square_list([1,2,3])

    #4
    fibonacci_stop(30)

    #5
    x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
    status = [1, 0, 0, 0]  # status signal
    clean_pitch(x, status)
