
from functions import greet, goldilocks, square_list, fibonacci_stop, clean_pitch

# 1. Write a simple function
greet('world')

# 2. If/else statements
goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

# 3. For loops
print(square_list([1,2,3]))

# 4. While loops
print(fibonacci_stop(30))

#5. Logical operators
x = [-1,2,6,95] # "raw" pitch anble at four time steps
status = [1,0,0,0] # status signal
print(clean_pitch(x,status))

